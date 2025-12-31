from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 27806628))
        self.API_HASH = getenv("API_HASH","25d88301e886b82826a525b7cf52e090")

        self.BOT_TOKEN = getenv("BOT_TOKEN","8577192556:AAH_VGCGYNA_s-_NFXeyXMb12_J7UIGK4Og")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Bosshub:JMaff0WvazwNxKky@cluster0.l0xcoc1.mongodb.net/?appName=Cluster0")

        self.LOGGER_ID = int(getenv("LOGGER_ID",-1003369263462))
        self.OWNER_ID = int(getenv("OWNER_ID", 8525952693))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", BQF1s6cAiH_ojYTnUQ1NsyFD1Ulhf7VfMSYaa0VbaHky0PDjO8UyRtV1shBhOMegzTsXXt-ooUZRaiiGvWYmmjalNyBYzNHQjAumEJYbCbyGRl5RJGJdSupmiQBa3dR34AnKDc2_fNzp6PGsWk-qKlzZT8DhaFAlxDZmaha0GwPjmm8aYZlle1UsyZLbM_vx14nmHJT8gyGMbmifTxXh-JpL3_AaRCbnW9jLh0ULf_CSURvd7lg8gc578_4H0KvwSBtIYuyohvmyRC2kKX0-vQCn7X_MfFzqsxrQvdi2yYNWW5WgmzQID91602_GqPQ1-DzSOx5f7wNBPAmqTQ_uvxO5Ww-fLgAAAAGx9uaUAA)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
