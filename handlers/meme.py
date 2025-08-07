from aiogram import Bot, Router, types
import logging

from services.meme_llm import get_meme_text
from utils.image_gen import make_meme
import random
import os
from aiogram.types import FSInputFile
from services.meme_llm import get_meme_text

logger = logging.getLogger(__name__)

router = Router()

@router.callback_query()
async def button_callback_query(callback: types.CallbackQuery):
    await callback.answer("...", reply_markup=types.ReplyKeyboardRemove())

@router.message()
async def meme_request_handler(message: types.Message):
    text = message.text.lower()

    if text.startswith('мем про'):
        logger.info(f'Поступил запрос на мем: {message.text}')
        topic = text.replace('мем про', '').strip()
        if not topic:
            await message.answer('Дурачелла, ты забыл тему для ржаки.'
                                 '\nНапимер: мем про кота')
        else: #Вызов ЛЛМ
            await message.answer(f"Окей! Придумываю мем про: {topic} 🧠💥")
            # Выбираем случайный шаблон
            templates = os.listdir("imagestempl")
            template = random.choice(templates)
            output_path = "output/meme.jpg"  # можно рандомизировать имя

            meme_text = await get_meme_text(topic)
            make_meme(f"imagestempl/{template}", meme_text, output_path)

            # Отправляем картинку как фото
            output_path = "output/meme.jpg"
            photo = FSInputFile(output_path)
            await message.answer_photo(photo, caption=f"Мем на тему: {topic}")
    else:
        await message.answer("Я умею делать мемы. Напиши: мем про ...")