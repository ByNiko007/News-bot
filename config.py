import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "")
CHECK_INTERVAL_MINUTES = 15

RSS_FEEDS = [
    {
        "name": "Kripto Kurdu",
        "url": "https://rsshub.app/telegram/channel/kriptokurduhaber",
        "category": "🪙 Kripto",
        "emoji": "🐺"
    },
]
