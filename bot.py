import asyncio
import logging
from telegram_reader import main

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    asyncio.run(main())
