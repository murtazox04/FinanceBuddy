from enum import Enum
from aiogram.filters.callback_data import CallbackData


class CurrencyType(Enum):
    USD = "USD"
    UZS = "UZS"
    RUB = "RUB"
    EUR = "EUR"


class Currency(CallbackData, prefix="currency"):
    currency: CurrencyType
