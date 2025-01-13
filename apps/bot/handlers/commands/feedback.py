from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command('notifications'))
async def cmd_notifications(message: Message):
    text = "Fikr-mulohaza qoldirish uchun quyidagilardan birini tanlang:"
    markup = ...
    await message.answer(text, reply_markup=markup)

