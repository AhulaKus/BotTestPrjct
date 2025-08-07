import asyncio
from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN
from handlers import routers
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


async def main():
        for router in routers:
            dp.include_router(router)
        await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
