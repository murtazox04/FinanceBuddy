from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from apps.bot.keyboards.inline import language_keyboard
from apps.bot.keyboards.default import main_menu_keyboard
from apps.bot.states.main_menu import MainMenu as MainMenuState
from apps.users.models import User, update_or_create_user

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_exists = await User.objects.filter(id=user_id).aexists()
    if user_exists:
        text = "Assalomu alaykum! FinanceBunny botiga xush kelibsiz! Boshlash uchun menyudan tanlang."
        markup = main_menu_keyboard()
        await state.set_state(MainMenuState.menu)
    else:
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = message.from_user.username
        await update_or_create_user(user_id, first_name=first_name, last_name=last_name, username=username)
        text = (
            "Assalomu alaykum! FinanceBunny botiga xush kelibsiz! "
            "Moliyaviy boshqaruvingizni osonlashtiramiz. Boshlash uchun kerakli tilni tanlang."
        )
        markup = language_keyboard()
    await message.answer(text, reply_markup=markup)
