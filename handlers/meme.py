from aiogram import Bot, Router, types

router = Router()

@router.message()
async def meme_request_handler(message: types.Message):
    text = message.text.lower()

    if text.startswith('мем про'):
        topic = text.replace('мем про', '').strip()
        if not topic:
            await message.answer('Долбаджобус, ты забыл тему для ржаки.'
                                 '\nНапимер: мем про кота')
        else: #Вызов ЛЛМ
            await message.answer(f"Окей! Придумываю мем про: {topic} 🧠💥")
    else:
        await message.answer("Я умею делать мемы. Напиши: мем про ...")