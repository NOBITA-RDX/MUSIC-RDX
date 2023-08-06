from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ✯",
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
                text="✯Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ Hᴇʟᴩ & Cᴏᴍᴍᴀɴᴅs ✯", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ Sᴜᴩᴩᴏʀᴛ ✯", url="https://t.me/HORRIBLE_STUDY"
            ),
            InlineKeyboardButton(
                text="✯ Oᴡɴᴇʀ ✯", user_id="1777270311"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ Sᴏᴜʀᴄᴇ ✯", url="https://t.me/RDX_SERVER"
            ),
            InlineKeyboardButton(
                text="✯ Cʜᴀᴛᴛɪɴɢ ✯", url="https://t.me/FriendsVempire"
                )
        ],
        [
            InlineKeyboardButton(
                text="✯ Yᴏᴜᴛᴜʙᴇ ✯", url="https://youtube.com/@LofiBoyraj"  
            )
        ],
     ]
    return buttons
