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
                text="ᴀᴅᴅ ᴛᴏ ᴄʜᴀɴɴᴇʟ",
                url=f"https://t.me/{BOT_USERNAME}?startchannel=new",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʜ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴛᴏ ᴄʜᴀɴɴᴇʟ",
                url=f"https://t.me/{BOT_USERNAME}?startchannel=new",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💙", url="https://t.me/+xWcg-WBN1oBjMjk1"),
            InlineKeyboardButton(
                text="💚", url="https://t.me/+GEooO-YpKXlhNjA1"),
            InlineKeyboardButton(
                text="🖤", user_id="1777270311"),
            InlineKeyboardButton(
                text="💛", url="https://t.me/+FTpq6AVRnqMwZDRl"),
            InlineKeyboardButton(
                text="💜", url="https://youtube.com/@LofiBoyraj"
            ),
        ],
     ]
    return buttons
