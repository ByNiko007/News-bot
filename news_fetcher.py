import feedparser
import aiohttp
import asyncio
import json
import os
import hashlib
import logging
from datetime import datetime, timezone
from deep_translator import GoogleTranslator
from config import RSS_FEEDS

logger = logging.getLogger(__name__)

SENT_FILE = "sent_articles.json"


def load_sent_ids() -> set:
    if os.path.exists(SENT_FILE):
        with open(SENT_FILE, "r") as f:
            return set(json.load(f))
    return set()


def save_sent_ids(ids: set):
    with open(SENT_FILE, "w") as f:
        json.dump(list(ids), f)


def make_article_id(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()


def translate_to_az(text: str) -> str:
    try:
        if not text or len(text.strip()) < 3:
            return text
        translated = GoogleTranslator(source="auto", target="az").translate(text[:4500])
        return translated or text
    except Exception as e:
        logger.warning(f"Tərcümə xətası: {e}")
        return text


async def fetch_feed(session: aiohttp.ClientSession, feed_config: dict) -> list:
    articles = []
    try:
        async with session.get(feed_config["url"], timeout=aiohttp.ClientTimeout(total=15)) as resp:
            content = await resp.text()
            parsed = feedparser.parse(content)

            for entry in parsed.entries[:5]:  # Hər saytdan max 5 xəbər
                url = entry.get("link", "")
                title = entry.get("title", "Başlıq yoxdur")
                summary = entry.get("summary", "")

                # HTML taglarını təmizlə
                import re
                summary = re.sub(r"<[^>]+>", "", summary)
                summary = summary[:300] + "..." if len(summary) > 300 else summary

                # Azərbaycan dilinə tərcümə et
                title_az = translate_to_az(title)
                summary_az = translate_to_az(summary)

                articles.append({
                    "id": make_article_id(url),
                    "title": title_az,
                    "url": url,
                    "summary": summary_az,
                    "source": feed_config["name"],
                    "category": feed_config["category"],
                    "emoji": feed_config["emoji"],
                })
    except Exception as e:
        logger.warning(f"{feed_config['name']} feed-i oxunmadı: {e}")
    return articles


class NewsFetcher:
    def __init__(self):
        self.sent_ids = load_sent_ids()

    async def fetch_all(self) -> list:
        new_articles = []

        async with aiohttp.ClientSession() as session:
            tasks = [fetch_feed(session, feed) for feed in RSS_FEEDS]
            results = await asyncio.gather(*tasks)

        for articles in results:
            for article in articles:
                if article["id"] not in self.sent_ids:
                    new_articles.append(article)
                    self.sent_ids.add(article["id"])

        # Köhnə ID-ləri sil (max 10000 saxla)
        if len(self.sent_ids) > 10000:
            self.sent_ids = set(list(self.sent_ids)[-5000:])

        if new_articles:
            save_sent_ids(self.sent_ids)

        return new_articles
