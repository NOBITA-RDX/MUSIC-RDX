from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ᴀᴅᴅ ᴛᴏ ᴄʜᴀɴɴᴇʟ✯",
                url=f"https://t.me/{BOT_USERNAME}?startchannel=new",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ Hᴇʟᴩ & Cᴏᴍᴍᴀɴᴅs ✯",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✯Sᴇᴛᴛɪɴɢs✯", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ᴀᴅᴅ ᴛᴏ ᴄʜᴀɴɴᴇʟ✯",
                url=f"https://t.me/{BOT_USERNAME}?startchannel=new",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs ✯", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ sᴜᴩᴩᴏʀᴛ ✯", url="https://t.me/HORRIBLE_STUDY"
            ),
            InlineKeyboardButton(
                text="✯ ᴏᴡɴᴇʀ ✯", user_id="1777270311"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ sᴏᴜʀᴄᴇ ✯", url="https://t.me/RDX_SERVER"
            ),
            InlineKeyboardButton(
                text="✯ ᴄʜᴀᴛᴛɪɴɢ ✯", url="https://t.me/FriendsVempire"
                )
        ],
        [
            InlineKeyboardButton(
                text="✯ ʏᴏᴜᴛᴜʙᴇ ✯", url="https://youtube.com/@LofiBoyraj"  
            )
        ],
     ]
    return buttons
