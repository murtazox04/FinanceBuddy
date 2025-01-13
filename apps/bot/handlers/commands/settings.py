from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command('settings'))
async def cmd_settings(message: Message):
    text = """
    Sozlamalar menyusi:
    1. Tilni o‘zgartirish.
    2. Valyutani o‘zgartirish.
    3. Bildirishnomalarni boshqarish.
    """
    markup = ...
    await message.answer(text, reply_markup=markup)
