import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "")
CHECK_INTERVAL_MINUTES = 15

RSS_FEEDS = [
    {"name": "CoinDesk", "url": "https://www.coindesk.com/arc/outboundfeeds/rss/", "category": "🪙 Kripto", "emoji": "🔶"},
    {"name": "Cointelegraph", "url": "https://cointelegraph.com/rss", "category": "🪙 Kripto", "emoji": "📡"},
    {"name": "CryptoNews", "url": "https://cryptonews.com/news/feed/", "category": "🪙 Kripto", "emoji": "🔷"},
    {"name": "Reuters Business", "url": "https://feeds.reuters.com/reuters/businessNews", "category": "📈 Səhm Bazarı", "emoji": "📰"},
    {"name": "MarketWatch", "url": "https://feeds.content.dowjones.io/public/rss/mw_topstories", "category": "📈 Səhm Bazarı", "emoji": "📊"},
    {"name": "Yahoo Finance", "url": "https://finance.yahoo.com/news/rssindex", "category": "📈 Səhm Bazarı", "emoji": "🏦"},
]
