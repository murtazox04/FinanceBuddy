from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="💳 Xarajat qo‘shish",
    )
    builder.button(
        text="📊 Statistikalarni ko‘rish",
    )
    builder.button(
        text="🎯 Maqsad qo‘yish",
    )
    builder.button(
        text="⚙️ Sozlamalar",
    )
    builder.button(
        text="❓ Yordam",
    )
    return builder.adjust(2).as_markup(resize_keyboard=True)
