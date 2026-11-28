import asyncio
import logging
import secrets
import time
from dataclasses import dataclass, field

import aiohttp
from aiohttp import web

LOGGER = logging.getLogger("AoiMusic.utils.stream.live_relay")


@dataclass
class _RelayEntry:
    token: str
    remote_url: str
    mode: str
    chat_id: int
    content_type: str
    ext: str
    created_at: float = field(default_factory=time.monotonic)
    closed: bool = False


class _LocalLiveRelay:
    """
    Loopback HTTP relay (http://127.0.0.1:<port>/live_relay/<token>.<ext>) that
    bridges HTTPS live streams via Python aiohttp into plain local HTTP for
    PyTgCalls/NTgCalls static-ffmpeg.

    Why: static-ffmpeg on Linux container nodes frequently fails TLS/HTTPS
    handshakes or drops chunked HTTPS streams, whereas Python aiohttp connects
    reliably and transparently reconnects if upstream blips.
    """

    def __init__(self) -> None:
        self._runner: web.AppRunner | None = None
        self._site: web.TCPSite | None = None
        self._port: int = 0
        self._lock = asyncio.Lock()
        self._entries: dict[str, _RelayEntry] = {}
        self._chat_tokens: dict[int, str] = {}
        self._client: aiohttp.ClientSession | None = None

    async def _get_client(self) -> aiohttp.ClientSession:
        if self._client is None or self._client.closed:
            connector = aiohttp.TCPConnector(limit=24, ttl_dns_cache=300)
            self._client = aiohttp.ClientSession(
                connector=connector,
                headers={"User-Agent": "AoiMusicBot/2.0"},
            )
        return self._client

    async def ensure_started(self) -> int:
        if self._port and self._runner is not None:
            return self._port
        async with self._lock:
            if self._port and self._runner is not None:
                return self._port
            app = web.Application()
            app.router.add_route("HEAD", "/live_relay/{token}", self._handle_relay)
            app.router.add_route("GET", "/live_relay/{token}", self._handle_relay)
            runner = web.AppRunner(app, access_log=None)
            await runner.setup()
            site = web.TCPSite(runner, host="127.0.0.1", port=0)
            await site.start()
            sockets = site._server.sockets if site._server else []
            if not sockets:
                raise RuntimeError("LocalLiveRelay failed to bind loopback socket")
            self._port = int(sockets[0].getsockname()[1])
            self._runner = runner
            self._site = site
            LOGGER.info("[LiveRelay] Loopback HTTP relay listening on 127.0.0.1:%d", self._port)
            return self._port

    def stop_chat(self, chat_id: int) -> None:
        tok = self._chat_tokens.pop(chat_id, None)
        if tok:
            entry = self._entries.pop(tok, None)
            if entry:
                entry.closed = True

    async def register(self, remote_url: str, mode: str = "audio", chat_id: int = 0) -> str:
        port = await self.ensure_started()
        if chat_id:
            self.stop_chat(chat_id)

        # Clean up stale entries older than 6 hours
        now = time.monotonic()
        for k, v in list(self._entries.items()):
            if v.closed or (now - v.created_at > 21600):
                self._entries.pop(k, None)

        low = remote_url.lower().split("?", 1)[0]
        if mode == "video" or low.endswith(".mp4"):
            ext = "mp4"
            ctype = "video/mp4"
        elif low.endswith(".aac"):
            ext = "aac"
            ctype = "audio/aac"
        else:
            ext = "mp3"
            ctype = "audio/mpeg"

        tok = f"lr_{secrets.token_hex(10)}"
        entry = _RelayEntry(
            token=tok,
            remote_url=remote_url,
            mode=mode,
            chat_id=chat_id,
            content_type=ctype,
            ext=ext,
        )
        self._entries[tok] = entry
        if chat_id:
            self._chat_tokens[chat_id] = tok

        # Quick HEAD/warm check so upstream LiveHub is ready before ffmpeg connects
        try:
            sess = await self._get_client()
            async with sess.head(
                remote_url,
                timeout=aiohttp.ClientTimeout(total=6),
                allow_redirects=True,
            ) as resp:
                ct = (resp.headers.get("Content-Type") or "").split(";")[0].strip()
                if ct:
                    entry.content_type = ct
        except Exception:
            pass

        local_url = f"http://127.0.0.1:{port}/live_relay/{tok}.{ext}"
        LOGGER.info("[LiveRelay] Registered %s -> %s", local_url, remote_url[:90])
        return local_url

    async def _handle_relay(self, request: web.Request) -> web.StreamResponse:
        raw_tok = (request.match_info.get("token") or "").strip()
        tok = raw_tok.rsplit(".", 1)[0] if "." in raw_tok else raw_tok
        entry = self._entries.get(tok)
        if not entry or entry.closed:
            return web.Response(status=404, text="Relay not found or stopped.")

        if request.method == "HEAD":
            return web.Response(
                status=200,
                headers={
                    "Content-Type": entry.content_type,
                    "Cache-Control": "no-cache, no-store",
                },
            )

        sess = await self._get_client()
        resp: web.StreamResponse | None = None
        retries = 0
        max_retries = 8

        try:
            while not entry.closed and retries <= max_retries:
                try:
                    timeout = aiohttp.ClientTimeout(total=None, sock_connect=12, sock_read=25)
                    async with sess.get(
                        entry.remote_url,
                        timeout=timeout,
                        allow_redirects=True,
                    ) as upstream:
                        if upstream.status != 200:
                            retries += 1
                            LOGGER.warning(
                                "[LiveRelay] Upstream HTTP %s for %s (retry %d/%d)",
                                upstream.status, tok, retries, max_retries,
                            )
                            await asyncio.sleep(min(1.0 * retries, 3.0))
                            continue

                        if resp is None:
                            ct = (upstream.headers.get("Content-Type") or entry.content_type).split(";")[0].strip()
                            resp = web.StreamResponse(
                                status=200,
                                headers={
                                    "Content-Type": ct or entry.content_type,
                                    "Cache-Control": "no-cache, no-store",
                                },
                            )
                            await resp.prepare(request)

                        got_bytes = False
                        async for chunk in upstream.content.iter_chunked(32768):
                            if entry.closed:
                                return resp
                            if not chunk:
                                continue
                            got_bytes = True
                            retries = 0
                            await resp.write(chunk)

                        if entry.closed:
                            break
                        if not got_bytes:
                            retries += 1
                            await asyncio.sleep(1.0)
                        else:
                            # Upstream closed cleanly (e.g. Heroku idle/restart) -> reconnect seamlessly!
                            retries += 1
                            LOGGER.info("[LiveRelay] Upstream EOF for %s — reconnecting (%d/%d)", tok, retries, max_retries)
                            await asyncio.sleep(0.5)

                except (ConnectionResetError, BrokenPipeError, asyncio.CancelledError):
                    break
                except Exception as exc:
                    retries += 1
                    LOGGER.warning("[LiveRelay] Stream error for %s (%d/%d): %s", tok, retries, max_retries, exc)
                    if resp is None and retries > 2:
                        return web.Response(status=502, text=f"Upstream live relay error: {exc}")
                    await asyncio.sleep(min(1.0 * retries, 3.0))
        finally:
            if resp is not None:
                try:
                    await resp.write_eof()
                except Exception:
                    pass

        if resp is None:
            return web.Response(status=502, text="Upstream live relay produced no data.")
        return resp


_relay = _LocalLiveRelay()


async def register_live_relay(remote_url: str, mode: str = "audio", chat_id: int = 0) -> str:
    if not isinstance(remote_url, str) or not remote_url.startswith(("http://", "https://")):
        return remote_url
    if "127.0.0.1" in remote_url or "localhost" in remote_url:
        return remote_url
    return await _relay.register(remote_url, mode=mode, chat_id=chat_id)


def stop_live_relay(chat_id: int) -> None:
    _relay.stop_chat(chat_id)
