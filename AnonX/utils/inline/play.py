import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX.utils.formatters import time_to_seconds


## After Edits with Timer Bar
## After Edits with Timer Bar

def time_to_sec(time: str):
    x = time.split(":")

    if len(x) == 2:
        min = int(x[0])
        sec = int(x[1])

        total_sec = (min*60) + sec
    elif len(x) == 3:
        hour = int(x[0])
        min = int(x[1])
        sec = int(x[2])

        total_sec = (hour*60*60) + (min*60) + sec

    return total_sec

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_sec(played)
    total_sec = time_to_sec(dur)

    x, y = str(round(played_sec/total_sec,1)).split(".")
    pos = int(y)

    line = "━"
    circle = "♪"

    bar = line*(pos-1)
    bar += circle
    bar += line*(10-len(bar))

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Sᴏᴜʀᴄᴇ✯", callback_data=f"PanelMarkup {videoid}|{chat_id}"
            ),
            InlineKeyboardButton(
                text="✯Oᴡɴᴇʀ✯", user_id="1777270311"
            ),
        ],
        [
            InlineKeyboardButton(

                text="↺",

                callback_data=f"ADMIN 1|{chat_id}"

            ),

            InlineKeyboardButton(

                text="↻",

                callback_data=f"ADMIN 2|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Sᴜᴘᴘᴏʀᴛ✯", url="https://t.me/HORRIBLE_STUDY"
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_sec(played)
    total_sec = time_to_sec(dur)

    x, y = str(round(played_sec/total_sec,1)).split(".")
    pos = int(y)

    line = "━"
    circle = "♪"

    bar = line*(pos-1)
    bar += circle
    bar += line*(10-len(bar))

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Cʟᴏsᴇ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯𝐂ʟᴏsᴇ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Sʜᴜғғʟᴇ✯",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="✯ Lᴏᴏᴩ ✯", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Cʟᴏsᴇ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Sᴜᴘᴘᴏʀᴛ✯", url="https://t.me/HORRIBLE_STUDY",
            ),
            InlineKeyboardButton(
                text="✯Cʜᴀɴɴᴇʟ✯", url="https://t.me/RDX_SERVER",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Pʟᴀʏʟɪsᴛ✯", callback_data=f"add_playlist {videoid}",
                ),
            InlineKeyboardButton(
                text="✯Oᴡɴᴇʀ✯", user_id="1777270311",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Yᴏᴜᴛᴜʙᴇ✯", url="https://youtube.com/@LofiBoyraj",
             ),
        ],
        [
            InlineKeyboardButton(
                text="✯Cʟᴏsᴇ✯",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Sᴜᴘᴘᴏʀᴛ✯", url="https://t.me/HORRIBLE_STUDY",
            ),
            InlineKeyboardButton(
                text="✯Cʟᴏsᴇ✯",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="✯Cʟᴏsᴇ✯", callback_data=f"close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Pʟᴀʏʟɪsᴛ✯", callback_data=f"add_playlist {videoid}",
                ),
            InlineKeyboardButton(
                text="✯Oᴡɴᴇʀ✯", user_id="1777270311",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Sᴜᴘᴘᴏʀᴛ✯", url="https://t.me/HORRIBLE_STUDY",
                ),
            InlineKeyboardButton(
                text="✯Cʜᴀɴɴᴇʟ✯", url="https://t.me/RDX_SERVER",
             ),
        ],
        [
            InlineKeyboardButton(
                text="✯Yᴏᴜᴛᴜʙᴇ✯", url="https://youtube.com/@LofiBoyraj",               
            )
        ],
    ]
    return buttons


## Cpanel Markup


def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Pʟᴀʏʟɪsᴛ✯", callback_data=f"add_playlist {videoid}"
                ),
            InlineKeyboardButton(
                text="✯Oᴡɴᴇʀ✯", user_id="1777270311"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯Sᴜᴘᴘᴏʀᴛ✯", url="https://t.me/HORRIBLE_STUDY"
                ),
            InlineKeyboardButton(
                text="✯Cʜᴀɴɴᴇʟ✯", url="https://t.me/RDX_SERVER"
             ),
        ],
        [
            InlineKeyboardButton(
                text="✯Yᴏᴜᴛᴜʙᴇ✯", url="https://youtube.com/@LofiBoyraj"
            ),
        ],
        [
        InlineKeyboardButton(

                text="↺",

                callback_data=f"ADMIN 1|{chat_id}"

            ),

            

            InlineKeyboardButton(

                text="✯Cʟᴏsᴇ✯", callback_data=f"close"

            ),

            InlineKeyboardButton(

                text="↻",

                callback_data=f"ADMIN 2|{chat_id}"
            ),
        ],
    ]
    return buttons

