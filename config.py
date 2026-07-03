import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "")
CHECK_INTERVAL_MINUTES = 15

RSS_FEEDS = [
    {
        "name": "Kripto Kurdu",
        "url": "https://rss.app/feeds/xQJCzjubp4wGVbMW.xml",
        "category": "🪙 Kripto",
        "emoji": "🐺"
    },
]
