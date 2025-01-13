from aiogram.utils.keyboard import InlineKeyboardBuilder

from apps.bot.callbacks.stats import Statistics as StatisticsCallback


def statistics_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📅 Haftalik",
        callback_data=StatisticsCallback(statistics_type="week").pack()
    )
    builder.button(
        text="📆 Oylik",
        callback_data=StatisticsCallback(statistics_type="month").pack()
    )
    builder.button(
        text="📆 Yillik",
        callback_data=StatisticsCallback(statistics_type="year").pack()
    )
    builder.button(
        text="📊 Umumiy",
        callback_data=StatisticsCallback(statistics_type="all").pack()
    )
    return builder.adjust(1).as_markup()
