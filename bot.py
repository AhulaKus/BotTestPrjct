import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

from aiogram import Bot, Dispatcher, types

dp = Dispatcher()

async def main():
        token = "7837211892:AAG_jMcoJIeEYoXBrLLiUIaE4pDq2U5hV0U"
        bot = Bot(token)
        await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
