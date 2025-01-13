from aiogram.utils.keyboard import InlineKeyboardBuilder

from apps.bot.callbacks.language import Language as LanguageCallback


def language_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🇺🇿 O'zbekcha",
        callback_data=LanguageCallback(language="uz").pack()
    )
    builder.button(
        text="🇷🇺 Русский",
        callback_data=LanguageCallback(language="ru").pack()
    )
    builder.button(
        text="🇺🇸 English",
        callback_data=LanguageCallback(language="en").pack()
    )
    builder.button(
        text="🇺🇿 Ўзбекча",
        callback_data=LanguageCallback(language="uz_cyrl").pack()
    )
    return builder.adjust(2).as_markup()
