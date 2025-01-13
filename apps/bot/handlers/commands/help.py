from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command('help'))
async def cmd_help(message: Message):
    text = """
    FinanceBunny botining imkoniyatlari:
    1. Xarajatlarni kuzatish.
    2. Moliyaviy maqsadlarni qo‘yish va kuzatish.
    3. Statistikalar va hisobotlarni ko‘rish.
    Quyidagi tugmalardan foydalanib kerakli yordamni tanlang.
    """
    markup = ...
    await message.answer(text, reply_markup=markup)
