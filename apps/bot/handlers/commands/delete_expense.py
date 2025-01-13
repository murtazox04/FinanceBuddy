from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command('delete_expense'))
async def cmd_delete_expense(message: Message):
    text = "O‘chirilishi kerak bo‘lgan xarajatni tanlang:"
    markup = ...
    await message.answer(text)

