from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐏ᴇʀsᴏɴᴀʟ",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="𝐆ʟᴏʙᴀʟ", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴛᴏᴘ 10 ᴘʟᴀʏʟɪsᴛs", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐏ᴇʀsᴏɴᴀʟ", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐆ʟᴏʙᴀʟ", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="𝐆ʀᴏᴜᴘ's", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐁ᴀᴄᴋ", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="𝐂ʟᴏsᴇ", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀ᴜᴅɪᴏ", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="𝐕ɪᴅᴇᴏ", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐁ᴀᴄᴋ", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="𝐂ʟᴏsᴇ", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴛᴏᴘ 10 ᴘʟᴀʏʟɪsᴛs", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐏ᴇʀsᴏɴᴀʟ", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐆ʟᴏʙᴀʟ", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="𝐆ʀᴏᴜᴘ's", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐁ᴀᴄᴋ", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="𝐂ʟᴏsᴇ", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐁ᴀᴄᴋ",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="𝐂ʟᴏsᴇ", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝐃ᴇʟᴇᴛᴇ",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐁ᴀᴄᴋ",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="𝐂ʟᴏsᴇ",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✯ 𝐂ʟᴏsᴇ ✯",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
