from typing import Optional
from aiogram.utils.keyboard import InlineKeyboardBuilder

from apps.bot.callbacks.menu import Expense as ExpenseCallback
from apps.finance.helpers import get_categories


# def back_button(builder=None):
#     if builder is None:
#         builder = InlineKeyboardBuilder()
#     builder.button(
#         text="⬅️ Orqaga",
#         callback_data=ExpenseCallback(category_type="back").pack()
#     )
#     return builder


def expense_catategory_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📂 Umumiy Kategoriyalar",
        callback_data=ExpenseCallback(category_type="main").pack(),
    )
    builder.button(
        text="📁 Subkategoriyalar",
        callback_data=ExpenseCallback(category_type="subcategories").pack(),
    )
    builder.button(
        text="🔍 Kategoriya qidirish",
        callback_data=ExpenseCallback(category_type="search").pack(),
    )
    return builder.adjust(2).as_markup()


async def expense_main_category_keyboard(
    menu, _id, user_id, parent_id
) -> Optional[InlineKeyboardBuilder]:
    builder = InlineKeyboardBuilder()
    main_categories = await get_categories(
        _id=_id, user_id=user_id, parent_id=parent_id
    )
    if not main_categories:
        return None
    for category in main_categories:
        category_name = (
            category.name if len(category.name) <= 30 else category.name[:27] + "..."
        )
        builder.button(
            text=category_name,
            callback_data=ExpenseCallback(
                category_type=menu, category_id=category.pk
            ).pack(),
        )
    builder.button(
        text="➕ Kategoriya qo‘shish",
        callback_data=ExpenseCallback(category_type="add_category").pack(),
    )
    builder.button(
        text="⬅️ Orqaga", callback_data=ExpenseCallback(category_type="back").pack()
    )
    return builder.adjust(2, 1, 1).as_markup()


def expense_search_keyboard(search_text) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=f"🔍 {search_text}",
        callback_data=ExpenseCallback(menu="search", search_text=search_text).pack(),
    )
    return builder.adjust(2).as_markup()
