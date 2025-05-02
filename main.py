from src.messages import router1
import asyncio
import logging
import sys
from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
if not TOKEN:
    with open(".env", "w") as file:
        TOKEN = input("Enter token bot:\n")
        file.write(f"BOT_TOKEN={TOKEN}")


dp = Dispatcher()
dp.include_routers(router1)


async def main() -> None:
    bot = Bot(token=str(TOKEN))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
