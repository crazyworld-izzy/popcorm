import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "20185438"))
API_HASH = getenv("API_HASH", "c8f3cb6db40e4eb6e7e43866660e54ac")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8016992775:AAFo8yxC8GLWqrRYGoKlrr6NTBDzQn3FC-c")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME", "popcorn_008")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME", "Love_beatz_bot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME", "Love beats")
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://monivps5:monivps5@cluster0.kmbq8we.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002354592685))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7712969541))


# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Marwin040/Popcorn-",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Marz_dp")
SUPPORT_CHAT = getenv("SUPPORT_CHAT","https://t.me/moonz_lightx")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 555))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQE0AV4AkOHlEGUXTgnIHKVyXCxOGFcqn-m08At2L9-B0CEc_Q0egqoWYbJwtSOC9OCb68BrLjaB3Sip0W2KOBXvUcuL5Z-z3X1ul7U77kQx_AN7mdKVZBbigJ5NevVKTyOl3_9FwU2dCykolAlcLoKEQiXVTQ-xlVPO4OnhviNDSLDklbvTRAT54LxBLHp383Aqotr1UwAGg9rWt-HdKcJQc5NBw2SMigHrqIXqJA60sQiioG1wntXywli1_LvzFA7eGvGGQ3W5KEBp-RXE55DqK-JLz8rCCqpmqX5DiL4jbnpm8Gg0u5Blg2zCxCAKC7dDhobGvQFCnoxDpxu2y5yRdolDXwAAAAHLupNFAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://i.ibb.co/f4bS7Vr/photo-2024-10-11-18-28-48-7424588661833859176.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.ibb.co/f4bS7Vr/photo-2024-10-11-18-28-48-7424588661833859176.jpg"
)
PLAYLIST_IMG_URL = "https://i.ibb.co/f4bS7Vr/photo-2024-10-11-18-28-48-7424588661833859176.jpg"
STATS_IMG_URL = "https://i.ibb.co/f4bS7Vr/photo-2024-10-11-18-28-48-7424588661833859176.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/f4bS7Vr/photo-2024-10-11-18-28-48-7424588661833859176.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/f4bS7Vr/photo-2024-10-11-18-28-48-7424588661833859176.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
