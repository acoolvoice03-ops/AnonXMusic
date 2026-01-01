from os import getenv
from dotenv import load_dotenv

load_dotenv()

# ---------------- HELPERS ---------------- #

def get_int(var, default=0):
    try:
        return int(getenv(var, default))
    except (TypeError, ValueError):
        return default

def get_str(var, default=None):
    return getenv(var, default)

def get_bool(var, default=False):
    val = getenv(var)
    if val is None:
        return default
    return val.lower() in ("true", "1", "yes", "on")

# ---------------- CONFIG ---------------- #

class Config:
    def __init__(self):

        # Telegram API
        self.API_ID = get_int("API_ID", 29198115))
        self.API_HASH = get_str("API_HASH","c95739ca773e2e35efe11b406b59af3b")

        # Bot
        self.BOT_TOKEN = get_str("BOT_TOKEN","8577192556:AAH_VGCGYNA_s-_NFXeyXMb12_J7UIGK4Og")

        # Database
        self.MONGO_URL = get_str("MONGO_URL","mongodb+srv://Bossaahubdb:pmDPc44XLRB097vm@cluster0.unuj1k8.mongodb.net/?appName=Cluster0")

        # Owner & Logger
        self.OWNER_ID = get_int("OWNER_ID", 8525952693))
        self.LOGGER_ID = get_int("LOGGER_ID", 0)  # 0 = disabled (NO CRASH)

        # Assistant Sessions
        self.SESSION1 = get_str("SESSION")
        self.SESSION2 = get_str("SESSION2")
        self.SESSION3 = get_str("SESSION3")

        # Limits
        self.DURATION_LIMIT = get_int("DURATION_LIMIT", 60) * 60
        self.QUEUE_LIMIT = get_int("QUEUE_LIMIT", 20)
        self.PLAYLIST_LIMIT = get_int("PLAYLIST_LIMIT", 20)

        # Features
        self.AUTO_END = get_bool("AUTO_END", False)
        self.AUTO_LEAVE = get_bool("AUTO_LEAVE", False)
        self.VIDEO_PLAY = get_bool("VIDEO_PLAY", True)

        # Support
        self.SUPPORT_CHANNEL = get_str("SUPPORT_CHANNEL")
        self.SUPPORT_CHAT = get_str("SUPPORT_CHAT")

        # Images
        self.DEFAULT_THUMB = get_str(
            "DEFAULT_THUMB",
            "https://te.legra.ph/file/3e40a408286d4eda24191.jpg"
        )
        self.PING_IMG = get_str(
            "PING_IMG",
            "https://files.catbox.moe/haagg2.png"
        )
        self.START_IMG = get_str(
            "START_IMG",
            "https://files.catbox.moe/zvziwk.jpg"
        )

        # Cookies
        self.COOKIES_URL = [
            url for url in get_str("COOKIES_URL", "").split()
            if "batbin.me" in url
        ]

    # ---------------- CHECK ---------------- #

    def check(self):
        required = [
            "API_ID",
            "API_HASH",
            "BOT_TOKEN",
            "MONGO_URL",
            "OWNER_ID",
            "SESSION1",
        ]

        missing = [var for var in required if not getattr(self, var)]

        if missing:
            raise SystemExit(
                f"❌ Missing required environment variables: {', '.join(missing)}"
            )
