import asyncio
from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN
from handlers import routers

dp = Dispatcher()

async def main():
        bot = Bot(BOT_TOKEN)
        for router in routers:
            dp.include_router(router)
        await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
