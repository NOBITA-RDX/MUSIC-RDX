from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐇ᴇʟᴩ ✯",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✯𝐒ᴇᴛᴛɪɴɢs✯", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐇ᴇʟᴩ ✯", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐒ᴜᴩᴩᴏʀᴛ ✯", url="https://t.me/HORRIBLE_STUDY"
            ),
            InlineKeyboardButton(
                text="✯ 𝐎ᴡɴᴇʀ ✯", user_id="1777270311"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐒ᴏᴜʀᴄᴇ ✯", url="https://t.me/RDXXDSERVER"
            ),
            InlineKeyboardButton(
                text="✯ 𝐂ʜᴀᴛᴛɪɴɢ ✯", url="https://t.me/TERIMERIYAAARIYAN"  
                )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐘ᴏᴜᴛᴜʙᴇ ✯", url="https://youtube.com/@LofiBoyraj"  
            )
        ],
     ]
    return buttons
