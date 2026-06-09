import asyncio
import logging
from telegram import Bot
from telegram.constants import ParseMode
from config import CHANNEL_ID

logger = logging.getLogger(__name__)


def format_message(article: dict) -> str:
    title = article["title"]
    summary = article.get("summary", "")
    url = article["url"]
    source = article["source"]
    category = article["category"]
    emoji = article["emoji"]

    msg = f"{emoji} <b>{title}</b>\n\n"

    if summary:
        msg += f"📝 {summary}\n\n"

    msg += f"🏷 {category} | 🌐 {source}\n"
    msg += f"🔗 <a href='{url}'>Tam oxu</a>"

    return msg


class NewsSender:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def send_articles(self, articles: list):
        for article in articles:
            try:
                text = format_message(article)
                await self.bot.send_message(
                    chat_id=CHANNEL_ID,
                    text=text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=False,
                )
                await asyncio.sleep(2)  # Flood limitindən qorunmaq üçün
            except Exception as e:
                logger.error(f"Xəbər göndərilmədi ({article.get('title', '')}): {e}")
