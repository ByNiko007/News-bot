import asyncio
import logging
from telethon import TelegramClient, events
from deep_translator import GoogleTranslator
from telegram import Bot
from config import API_ID, API_HASH, BOT_TOKEN, CHANNEL_ID, SOURCE_CHANNEL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def translate_to_az(text: str) -> str:
    try:
        if not text or len(text.strip()) < 3:
            return text
        translated = GoogleTranslator(source="auto", target="az").translate(text[:4500])
        return translated or text
    except Exception as e:
        logger.warning(f"Tərcümə xətası: {e}")
        return text


async def main():
    bot = Bot(token=BOT_TOKEN)
    client = TelegramClient("session", int(API_ID), API_HASH)

    await client.start()
    logger.info("Telegram oxuyucu işə düşdü!")

    @client.on(events.NewMessage(chats=SOURCE_CHANNEL))
    async def handler(event):
        text = event.message.text
        if not text:
            return

        logger.info(f"Yeni post: {text[:50]}...")
        translated = translate_to_az(text)

        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"📨 {translated}",
        )
        logger.info("Göndərildi!")

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
