from aiogram.utils.keyboard import InlineKeyboardBuilder

from apps.bot.callbacks.currency import Currency as CurrencyCallback


def currency_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="💵 USD(Dollar)",
        callback_data=CurrencyCallback(currency="USD").pack()
    )
    builder.button(
        text="💴 UZS(O'zbek so'mi)",
        callback_data=CurrencyCallback(currency="UZS").pack()
    )
    builder.button(
        text="💶 EUR(Euro)",
        callback_data=CurrencyCallback(currency="EUR").pack()
    )
    builder.button(
        text="💷 RUB(Rubl)",
        callback_data=CurrencyCallback(currency="RUB").pack()
    )
    return builder.adjust(2).as_markup()
