import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import Bot
from config import BOT_TOKEN, CHECK_INTERVAL_MINUTES
from news_fetcher import NewsFetcher
from news_sender import NewsSender

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def fetch_and_send(fetcher: NewsFetcher, sender: NewsSender):
    logger.info("Xəbərlər yoxlanılır...")
    articles = await fetcher.fetch_all()
    if articles:
        await sender.send_articles(articles)
        logger.info(f"{len(articles)} yeni xəbər göndərildi.")
    else:
        logger.info("Yeni xəbər tapılmadı.")


async def main():
    bot = Bot(token=BOT_TOKEN)
    fetcher = NewsFetcher()
    sender = NewsSender(bot)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        fetch_and_send,
        "interval",
        minutes=CHECK_INTERVAL_MINUTES,
        args=[fetcher, sender],
    )
    scheduler.start()

    logger.info(f"Bot işə düşdü. Hər {CHECK_INTERVAL_MINUTES} dəqiqədən bir yoxlanılacaq.")
    await fetch_and_send(fetcher, sender)

    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())
