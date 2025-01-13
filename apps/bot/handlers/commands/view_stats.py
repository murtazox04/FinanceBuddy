from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command('view_stats'))
async def cmd_view_stats(message: Message):
    text = """
    Statistikalar bo‘yicha tanlov:
    1. Oylik xarajatlar.
    2. Kategoriyalar bo‘yicha taqsimot.
    3. Daromad va xarajat taqqoslash.
    """
    markup = ...
    await message.answer(text, reply_markup=markup)

