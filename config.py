# ==========================================
#   KONFİQURASİYA - Bura öz məlumatlarını yaz
# ==========================================

# BotFather-dan aldığın token
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Xəbərlərin göndəriləcəyi kanalın ID-si (məs: @mychannelname və ya -100123456789)
CHANNEL_ID = "@your_channel_here"

# Neçə dəqiqədən bir yoxlasın
CHECK_INTERVAL_MINUTES = 15

# ==========================================
#   RSS FEED-LƏR
# ==========================================
RSS_FEEDS = [
    # --- KRİPTOVALYUTA ---
    {
        "name": "CoinDesk",
        "url": "https://www.coindesk.com/arc/outboundfeeds/rss/",
        "category": "🪙 Kripto",
        "emoji": "🔶"
    },
    {
        "name": "CryptoNews",
        "url": "https://cryptonews.com/news/feed/",
        "category": "🪙 Kripto",
        "emoji": "🔷"
    },
    {
        "name": "Cointelegraph",
        "url": "https://cointelegraph.com/rss",
        "category": "🪙 Kripto",
        "emoji": "📡"
    },
    {
        "name": "Bitcoin Magazine",
        "url": "https://bitcoinmagazine.com/feed",
        "category": "🪙 Kripto",
        "emoji": "₿"
    },

    # --- SƏHM BAZARI ---
    {
        "name": "Reuters Business",
        "url": "https://feeds.reuters.com/reuters/businessNews",
        "category": "📈 Səhm Bazarı",
        "emoji": "📰"
    },
    {
        "name": "MarketWatch",
        "url": "https://feeds.content.dowjones.io/public/rss/mw_topstories",
        "category": "📈 Səhm Bazarı",
        "emoji": "📊"
    },
    {
        "name": "Investing.com",
        "url": "https://www.investing.com/rss/news.rss",
        "category": "📈 Səhm Bazarı",
        "emoji": "💹"
    },
    {
        "name": "Yahoo Finance",
        "url": "https://finance.yahoo.com/news/rssindex",
        "category": "📈 Səhm Bazarı",
        "emoji": "🏦"
    },
]
