from aiogram.filters.callback_data import CallbackData

class Language(CallbackData, prefix="language"):
    language: str
