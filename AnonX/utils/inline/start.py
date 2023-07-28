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
                text="✯ 𝐒ᴜᴩᴩᴏʀᴛ ✯", chat_id="-1001834682067"
            ),
            InlineKeyboardButton(
                text="✯ 𝐎ᴡɴᴇʀ ✯", user_id="1777270311"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐒ᴏᴜʀᴄᴇ ✯", chat_id="-1001952227898"
            ),
            InlineKeyboardButton(
                text="✯ 𝐂ʜᴀᴛᴛɪɴɢ ✯", -1001952227898  
                )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐘ᴏᴜᴛᴜʙᴇ ✯", url="https://youtube.com/@LofiBoyraj"  
            )
        ],
     ]
    return buttons
