import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

from aiogram import Bot, Dispatcher, types
from httpx import Client

dp = Dispatcher()


@dp.message(Command('start'))
async def start_command (message: types.Message) -> None:
    await message.answer('Привет! Я бот, который может создавать ржака-мэмасы. \nТак что, Хузлик, пиши сюда свой понос, я сделаю конфэтку.')

@dp.message(Command('help'))
async def help_command (message: types.Message) -> None:
    await message.answer('Дэбик, напиши "мем про..." и тему от себя добавь. Всё просто \nИспользуемые модели:...(добавить)')


@dp.message()
async def meme_request_handler(message: types.Message):
    user_text = message.text.lower()

    if user_text.startswith("мем про"):
        topic = user_text.replace("мем про", "").strip()
        if not topic:
            await message.answer("Ты забыл тему мема! Напиши, например: 'мем про кота'")
            return

        # Заглушка — генерация мема
        await message.answer(f"Окей! Придумываю мем про: {topic} 🧠💥")
        # Тут будет вызов LLM + генерация изображения

    else:
        await message.answer("Я умею делать мемы. Напиши: мем про ...")


async def main() -> None:
    token = "7837211892:AAG_jMcoJIeEYoXBrLLiUIaE4pDq2U5hV0U"
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
