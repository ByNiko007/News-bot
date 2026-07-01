import asyncio
import logging
import os
from aiohttp import web
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


async def fetch_and_send(fetcher, sender):
    logger.info("Xəbərlər yoxlanılır...")
    articles = await fetcher.fetch_all()
    if articles:
        await sender.send_articles(articles)
        logger.info(f"{len(articles)} yeni xəbər göndərildi.")
    else:
        logger.info("Yeni xəbər tapılmadı.")


async def health(request):
    return web.Response(text="OK")


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

    await fetch_and_send(fetcher, sender)

    app = web.Application()
    app.router.add_get("/", health)
    port = int(os.environ.get("PORT", 8080))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    logger.info(f"Bot işə düşdü. Port: {port}")

    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())
