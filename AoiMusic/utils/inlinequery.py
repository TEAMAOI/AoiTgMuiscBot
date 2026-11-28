import inspect

from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

_ARTICLE_THUMB_KEY = (
    "thumb_url"
    if "thumb_url" in inspect.signature(InlineQueryResultArticle.__init__).parameters
    else "thumbnail_url"
)


def _article(title: str, description: str, thumb: str, command_text: str) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        title=title,
        description=description,
        **{_ARTICLE_THUMB_KEY: thumb},
        input_message_content=InputTextMessageContent(command_text),
    )


answer = [
    _article(
        "ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ",
        "ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ.",
        "https://te.legra.ph/file/7345db59ab5d2c5cb142a.jpg",
        "/pause",
    ),
    _article(
        "ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ",
        "ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ.",
        "https://te.legra.ph/file/9fe24bde84b1d31f685a9.jpg",
        "/resume",
    ),
    _article(
        "ᴍᴜᴛᴇ sᴛʀᴇᴀᴍ",
        "ᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ",
        "https://te.legra.ph/file/c03f25028fa248401d519.jpg",
        "/vcmute",
    ),
    _article(
        "ᴜɴᴍᴜᴛᴇ sᴛʀᴇᴀᴍ",
        "ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ",
        "https://te.legra.ph/file/98622051acad1988886be.jpg",
        "/vcunmute",
    ),
    _article(
        "sᴋɪᴘ sᴛʀᴇᴀᴍ",
        "sᴋɪᴘ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ. | sᴋɪᴘ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ. | ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴛʀᴀᴄᴋ ɴᴜᴍʙᴇʀ: /skip [number] ",
        "https://te.legra.ph/file/1b78431fe8de0e497c188.jpg",
        "/skip",
    ),
    _article(
        "ᴇɴᴅ sᴛʀᴇᴀᴍ",
        "sᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴏɴɢ ᴏɴ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇᴄʜᴀᴛ.",
        "https://te.legra.ph/file/d3663021fb51e14a84aa9.jpg",
        "/stop",
    ),
    _article(
        "sʜᴜғғʟᴇ sᴛʀᴇᴀᴍ",
        "sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.",
        "https://te.legra.ph/file/3d130381bf5945c139023.jpg",
        "/shuffle",
    ),
    _article(
        "sᴇᴇᴋ sᴛʀᴇᴀᴍ",
        "sᴇᴇᴋ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ ᴛᴏ ᴀ sᴘᴇᴄɪғɪᴄ ᴅᴜʀᴀᴛɪᴏɴ.",
        "https://te.legra.ph/file/c66abbf490158487fdb72.jpg",
        "/seek 10",
    ),
    _article(
        "ʟᴏᴏᴘ sᴛʀᴇᴀᴍ",
        "ʟᴏᴏᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ. ᴜsᴀsɢᴇ: /loop [enable|disable]",
        "https://te.legra.ph/file/f739e6067725fa88ce8d3.jpg",
        "/loop 3",
    ),
]
