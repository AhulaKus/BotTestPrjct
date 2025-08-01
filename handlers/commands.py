from mailbox import Message

from aiogram import Bot, Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def start_command(message: types.Message) -> None:
    await message.answer('Привет! Я бот, который может создавать ржака-мэмасы.'
                         '\nТак что, Гхузлик, пиши сюда свой понос, я сделаю конфэтку.')

@router.message(Command('help'))
async def help_command(message: types.Message) -> None:
    await message.answer('Дэбик, напиши "мем про..." и тему от себя добавь. Всё просто'
                         '\nИспользуемые модели:...(добавить)')
