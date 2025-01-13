from aiogram import types, Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from apps.bot.states.main_menu import MainMenu as MainMenuState
from apps.bot.callbacks.menu import Expense as ExpenseCallback
from apps.bot.keyboards.inline import (
    expense_main_category_keyboard, expense_catategory_keyboard, expense_search_keyboard,
)
from apps.finance.helpers import create_category

router = Router()


@router.message(MainMenuState.menu)
async def main_menu(message: types.Message, state: FSMContext):
    menu = message.text
    markup = None
    if menu == "💳 Xarajat qo‘shish":
        text = "Siz xarajat qo‘shmoqchisiz. Iltimos, kategoriyalarni ko‘rish uchun quyidagi variantlardan birini tanlang:"
        markup = expense_catategory_keyboard()
    elif menu == "📊 Statistikalarni ko‘rish":
        text = "Statistika"
        markup = None
    elif menu == "🎯 Maqsad qo‘yish":
        text = "Maqsad"
        markup = None
    elif menu == "⚙️ Sozlamalar":
        text = "Sozlamalar"
        markup = None
    elif menu == "❓ Yordam":
        text = "Yordam"
        markup = None
    else:
        return
    await state.clear()
    await message.answer(text, reply_markup=markup)


@router.callback_query(ExpenseCallback.filter())
async def expense_menu(call: CallbackQuery, callback_data: ExpenseCallback, state: FSMContext):
    user_id = call.from_user.id
    menu = callback_data.category_type
    category_id = callback_data.category_id
    markup = None
    if not menu in ["back", "add_category"]:
        if menu in ["main", "subcategories"]:
            markup = await expense_main_category_keyboard(menu, category_id, user_id, category_id if category_id else None)
        elif menu == "search":
            search_text = callback_data.get("search_text", "")
            markup = expense_search_keyboard(search_text)
        text = "Kategoriyalar ro‘yxatidan birini tanlang yoki qo'shing:"
        if markup:
            await call.message.edit_text(text, reply_markup=markup)
        else:
            await call.message.edit_text("Kategoriyalar topilmadi.")
    else:
        if menu == "back":
            text = "Siz xarajat qo‘shmoqchisiz. Iltimos, kategoriyalarni ko‘rish uchun quyidagi variantlardan birini tanlang:"
            markup = expense_catategory_keyboard()
        elif menu == "add_category":
            text = "Kategoriya nomini kiriting:"
            await state.set_state(MainMenuState.add_category)  # State belgilash
            markup = None  # Bu yerda markup kerak emas
        await call.message.edit_text(text, reply_markup=markup)
    await call.answer("Kategoriyalar ro‘yxati ko'rsatilmoqda.")


@router.message(MainMenuState.add_category)
async def add_category_menu(message: types.Message, state: FSMContext):
    category_name = message.text
    await create_category(category_name, message.from_user.id)
    await message.answer("Kategoriya muvaffaqiyatli qo‘shildi.")
