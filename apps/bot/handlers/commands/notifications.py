from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command('notifications'))
async def cmd_notifications(message: Message):
    text = """
    Bildirishnomalar sozlamalari:
    1. Moliyaviy maqsad bildirishnomalari.
    2. Eslatmalarni yoqish/o‘chirish.
    """
    markup = ...
    await message.answer(text, reply_markup=markup)

