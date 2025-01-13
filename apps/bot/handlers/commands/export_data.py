from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command('export_data'))
async def cmd_export_data(message: Message):
    text = "Qaysi formatda eksport qilishni tanlang:"
    markup = ...
    await message.answer(text)

