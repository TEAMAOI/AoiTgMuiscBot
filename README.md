<div align="center">

# 🎵 AoiMusic — Music & Group Management Bot

**A fast, all-in-one Telegram Voice Chat Music & Video Streaming + Full Group Management Bot**  
Powered by **Kurigram (2.2.27+)**, **PyTgCalls**, **Aoi Music API**, **MongoDB (Motor)**, and the **Musiciconis Premium Emoji Pack**.

<p>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11+" />
  </a>
  <a href="https://github.com/TEAMAOI/AoiTgMuiscBot">
    <img src="https://img.shields.io/badge/Kurigram-2.2.27%2B-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Kurigram 2.2.27+" />
  </a>
  <a href="https://www.mongodb.com/">
    <img src="https://img.shields.io/badge/MongoDB-Motor-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB" />
  </a>
</p>

<p>
  <a href="https://t.me/aoinetwork">
    <img src="https://img.shields.io/badge/Updates%20Channel-@aoinetwork-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Updates Channel" />
  </a>
  <a href="https://t.me/devpointserror">
    <img src="https://img.shields.io/badge/Support%20Group-@devpointserror-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Support Group" />
  </a>
</p>

</div>

---

## 🚀 One-Click Deploy

<p align="center">
  <a href="https://host-repository.vercel.app/deploy?template=https://github.com/TEAMAOI/AoiTgMuiscBot.git">
    <img src="https://host-repository.vercel.app/deploy-button.svg" alt="Deploy on Aoi Hosting" height="40" />
  </a>
  &nbsp;
  <a href="https://dashboard.heroku.com/new?template=https://github.com/TEAMAOI/AoiTgMuiscBot">
    <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" height="40" />
  </a>
</p>

---

## ✨ Key Features

### 🎶 HD Music & Video Streaming
- **Multi-Platform Support:** Stream audio (`/play`) and video (`/vplay`) in group & channel Voice Chats from **YouTube**, **Spotify**, **Apple Music**, **SoundCloud**, **JioSaavn**, **Resso**, **Live Radio**, and **Telegram Media**.
- **Smart Playback Controls:** `/pause`, `/resume`, `/skip`, `/end`, `/seek`, `/loop`, `/shuffle`, `/voteskip`, `/auth`, `/queue`, `/autoplay`, and `/playmode`.
- **Playlists, Lyrics & Charts:** Personal playlists (`/playlist`), live synced VC lyrics (`/lyrics`), per-chat trending tracks (`/hot`), song downloads (`/song`), and inline search.
- **Multi-Assistant Architecture:** Supports comma-separated `STRING_SESSIONS` for scaling across large numbers of groups.

### 🛡️ Native Group Management & Security Suite
All 12 management modules run natively on **Kurigram + async Motor MongoDB** with zero external SQL dependencies and zero conflicts with music commands:
- **Admins & Group Settings:** Promote/demote (`/promote`, `/fullpromote`, `/lowpromote`, `/demote`), custom titles, pins, invite links, group title/description/photo/sticker management, admin & bot lists.
- **Bans, Kicks & Remote Mod:** `/ban`, `/sban`, `/tban`, `/unban`, `/kick`, `/kickme`, plus sudo remote moderation (`/rban`, `/runban`, `/rkick`, `/rmute`, `/runmute`).
- **Smart Conflict-Free Muting:** `/mute`, `/tmute`, `/unmute` mute/unmute **users** when replying or passing `@user`/`id`, while bare `/mute` & `/unmute` seamlessly control **Voice Chat audio**.
- **Warnings System:** `/warn`, `/dwarn`, `/warns`, `/resetwarns`, `/warnlimit`, `/strongwarn` (`ban` / `kick` / `mute`) with an inline **Remove Warn** button.
- **Locks & Nightmode:** Lock 17 content types (`/lock`, `/unlock`, `/locks`, `/locktypes`) plus one-command `/nightmode` & `/rmnight`.
- **Purge & Auto-Delete:** Fast batch `/purge`, `/del`, plus scheduled auto-delete for media (`/mediadelete`) and messages (`/msgdelete`).
- **Word & Sticker Blacklists:** Keyword and sticker-pack blacklists with configurable punishments (`delete`, `mute`, `kick`, `ban`).
- **Advanced Security Guard:** Anti-Flood (`/setflood`), Bio-Link Guard (`/biolink`), Anti-Edit (`/antiedit`), Anti-Abuse (`/abuse`), NSFW Guard (`/nsfw`), Auto-Demote protection, Bluetext Cleaner (`/cleanblue`), and Anti-Banall Lockdown Trap (`banall` / `gcfree` / `/lockdown`).
- **Welcome, Goodbye & Join Requests:** Custom welcome/goodbye templates, clean-welcome, clean-service, `/welcomemute` (with inline **I Am Human** verification button), and `/joinrequest` (with inline **Approve / Dismiss** buttons).
- **Notes, Filters & Rules:** Save media/text notes (`/save`, `#notename`), auto-reply keyword filters (`/filter`, `/stopfilter`), and group rules (`/setrules`, `/rules`).
- **Group Tools & AFK:** Trusted user approval (`/approve`), admin reporting (`/report`, `@admin`), batch member mention (`/tagall`, `/canceltag`), moderation log channel (`/setlog`), PM group connection (`/connect`), JSON settings backup (`/export`, `/import`), user/chat `/id` & `/info`, and global AFK (`/afk`, `brb`).

### 💎 Musiciconis Premium Emoji UI
- Powered by the **Musiciconis** custom emoji pack (`99` unique icons via `AoiMusic/utils/premium_emoji.py`).
- Uses `<tg-emoji emoji-id="...">` in HTML cards and Telegram Bot API 9.4+ `icon_custom_emoji_id` on inline buttons with compact small-caps labels optimized for mobile screens.

---

## 🎧 Aoi Music API Integration

AoiMusic uses the **Aoi Hosting Music API** (`https://host-repository.vercel.app`) inside `AoiMusic/platforms/Youtube.py` as its primary streaming and download engine (with automatic `yt-dlp` fallback if no API key is set).

### Endpoints

| Endpoint | Media | Free Quota | Extra Usage | Response |
| :--- | :--- | :--- | :--- | :--- |
| `GET /api/audio/{video_id}` | MP3 Audio | **250 / day** | `0.001 Coins` / req | JSON `{ "ok": true, "url": "..." }` (or `302` with `?redirect=1`) |
| `GET /api/video/{video_id}` | MP4 Video | **50 / day** | `0.001 Coins` / req | JSON `{ "ok": true, "url": "..." }` (or `302` with `?redirect=1`) |

### Authentication

Pass your key via `MEDIA_API_KEY` (sent in `X-API-Key`, also supports `?key=` and `Authorization: Bearer`):

```env
MEDIA_API_URL=https://host-repository.vercel.app
MEDIA_API_KEY=aoi_music_your_api_key_here
```

### Status Codes
- `200` / `302` — Stream URL JSON or direct redirect (`?redirect=1`)
- `401` — Missing or invalid API key
- `402` — Balance below `0.001 Coins`
- `429` — Daily free limit reached (when *Use Coins* is OFF)
- `502` / `503` — Temporary backend error (auto-refunded)

---

## 📋 Command Overview

<details>
<summary><b>🎵 Music & Voice Chat Commands</b></summary>

| Command | Description |
| :--- | :--- |
| `/play`, `/vplay`, `/playforce` | Play audio or video in Voice Chat |
| `/cplay`, `/cvplay`, `/channelplay` | Stream music in a linked channel |
| `/pause`, `/resume`, `/skip`, `/end` | Control active Voice Chat playback |
| `/mute`, `/unmute` *(no args)* | Mute / unmute Voice Chat stream |
| `/queue`, `/shuffle`, `/loop`, `/seek` | Manage queue, loop, and seek position |
| `/playlist`, `/song`, `/lyrics`, `/hot` | Playlists, downloads, lyrics, and top tracks |
| `/auth`, `/unauth`, `/authusers` | Grant non-admins playback controls |
| `/settings`, `/playmode`, `/lang` | Configure group playback & language |

</details>

<details>
<summary><b>🛡️ Group Management & AFK Commands</b></summary>

| Module | Key Commands |
| :--- | :--- |
| **Admins** | `/promote`, `/fullpromote`, `/lowpromote`, `/demote`, `/title`, `/admins`, `/bots`, `/pin`, `/unpin`, `/pinned`, `/invitelink`, `/setgtitle`, `/setdesc`, `/setgpic`, `/delgpic`, `/setsticker` |
| **Bans** | `/ban`, `/sban`, `/tban`, `/unban`, `/kick`, `/kickme`, `/rban`, `/runban`, `/rkick`, `/rmute`, `/runmute` |
| **Muting** | `/mute`, `/tmute`, `/tempmute`, `/unmute` *(reply or pass `@user`/`id`)* |
| **Warns** | `/warn`, `/dwarn`, `/warns`, `/resetwarns`, `/warnlimit`, `/strongwarn` |
| **Locks** | `/lock`, `/unlock`, `/locks`, `/locktypes`, `/nightmode`, `/rmnight` |
| **Purge** | `/del`, `/purge`, `/mediadelete`, `/setmediadelay`, `/mediastatus`, `/msgdelete`, `/setmsgdelay`, `/msgstatus` |
| **Blacklists** | `/blacklist`, `/addblacklist`, `/unblacklist`, `/blacklistmode`, `/blsticker`, `/addblsticker`, `/unblsticker`, `/blstickermode` |
| **Security** | `/setflood`, `/setfloodmode`, `/flood`, `/biolink`, `/biofree`, `/antiedit`, `/abuse`, `/nsfw`, `/autodemote`, `/cleanblue`, `/lockdown`, `banall` / `gcfree` |
| **Welcome** | `/welcome`, `/goodbye`, `/setwelcome`, `/setgoodbye`, `/cleanwelcome`, `/cleanservice`, `/welcomemute`, `/joinrequest` |
| **Notes & Filters** | `/save`, `/get`, `/notes`, `/clear`, `#notename`, `/filter`, `/filters`, `/stopfilter`, `/rules`, `/setrules`, `/clearrules` |
| **Group Tools** | `/approve`, `/unapprove`, `/approved`, `/report`, `@admin`, `/tagall`, `/canceltag`, `/setlog`, `/connect`, `/export`, `/import`, `/disable`, `/enable`, `/id`, `/info` |
| **AFK** | `/afk [reason]`, `brb [reason]` |

</details>

<details>
<summary><b>👑 Owner & Sudo Commands</b></summary>

| Command | Description |
| :--- | :--- |
| `/addsudo`, `/delsudo`, `/sudolist` | Manage sudo users |
| `/gban`, `/ungban`, `/gbannedusers` | Global ban management |
| `/block`, `/unblock`, `/blacklistchat` | Block users or blacklist chats |
| `/broadcast`, `/gcast` | Broadcast messages to users/chats |
| `/stats`, `/gstats`, `/ping`, `/speedtest` | System metrics and latency checks |
| `/eval`, `/sh`, `/logs`, `/update`, `/restart` | Developer diagnostics & maintenance |

</details>

---

## 📁 Project Structure

```text
AoiMusic/
├── core/            # Kurigram bot client, PyTgCalls (AoiCall), userbot, MongoDB, Media API
├── platforms/       # YouTube (Aoi Music API + yt-dlp fallback), Spotify, Apple, SoundCloud, JioSaavn, Resso, Telegram
├── plugins/
│   ├── admins/      # VC playback admin controls (pause, resume, skip, stop, vcmute, seek, loop, auth)
│   ├── bot/         # /start, /help (unified Music + Management menu), /settings, /lyrics, /inline
│   ├── manage/      # 12 native Group Management & AFK modules (admins, bans, muting, warns, locks, purge, blacklists, security, welcome, notes_filters, group_utils, afk)
│   ├── misc/        # Auto-leave, cleanmode, seeker, join/leave hooks
│   ├── play/        # /play, /vplay, /cplay, autoplay, playlists, top tracks
│   ├── sudo/        # Global ban, sudoers, broadcast, Heroku/update tools, eval/shell
│   └── tools/       # Active VC, queue, radio, songs, speedtest, stats, languages
└── utils/           # manage_db.py, manage_helpers.py, premium_emoji.py (Musiciconis), rich_msg.py, thumbnails, database
config/              # Environment-based configuration (config.py)
strings/             # Multi-language strings & command definitions
```

---

## ⚙️ Environment Variables

| Variable | Required | Description |
| :--- | :---: | :--- |
| `API_ID` | Yes | Telegram API ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | Yes | Telegram API Hash from [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | Yes | Bot token from [@BotFather](https://t.me/BotFather) |
| `STRING_SESSIONS` | Yes | Pyrogram v2 string session(s) for VC assistant (comma-separated) |
| `MONGO_DB_URI` | Yes | MongoDB Atlas connection URI |
| `OWNER_ID` | Yes | Bot Owner numeric Telegram user ID |
| `LOGGER_ID` | Yes | Private log group ID (bot & assistant must be admins) |
| `MEDIA_API_KEY` | Recommended | Aoi Music API key from [Aoi Hosting](https://host-repository.vercel.app) |
| `MEDIA_API_URL` | Optional | Defaults to `https://host-repository.vercel.app` |
| `SUPPORT_CHANNEL` | Optional | Updates channel link (`https://t.me/aoinetwork`) |
| `SUPPORT_GROUP` | Optional | Support group link (`https://t.me/devpointserror`) |
| `SPOTIFY_CLIENT_ID` | Optional | Spotify API Client ID |
| `SPOTIFY_CLIENT_SECRET` | Optional | Spotify API Client Secret |
| `SET_CMDS` | Optional | Auto-register Telegram `/` menu commands (`True` by default) |

---

## 🛠️ Manual / VPS Setup

```bash
# 1. Clone the repository
git clone https://github.com/TEAMAOI/AoiTgMuiscBot.git
cd AoiTgMuiscBot

# 2. Install dependencies (Python 3.11+ & ffmpeg required)
pip install -r requirements.txt

# 3. Configure environment variables
cp .env.example .env
nano .env

# 4. Run the bot
python3 -m AoiMusic
```

### 🐳 Docker

```bash
docker build -t aoimusic .
docker run --env-file .env aoimusic
```

---

## 💬 Support & Community

<p align="center">
  <a href="https://t.me/aoinetwork">
    <img src="https://img.shields.io/badge/Updates%20Channel-@aoinetwork-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Updates Channel" />
  </a>
  <a href="https://t.me/devpointserror">
    <img src="https://img.shields.io/badge/Support%20Group-@devpointserror-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Support Group" />
  </a>
  <a href="https://github.com/TEAMAOI/AoiTgMuiscBot">
    <img src="https://img.shields.io/badge/GitHub-TEAMAOI%2FAoiTgMuiscBot-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Repo" />
  </a>
</p>

<div align="center">
Made with ❤️ by <b>TEAMAOI</b> • Licensed under the GNU General Public License
</div>
