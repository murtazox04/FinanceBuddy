from enum import Enum
from aiogram.filters.callback_data import CallbackData


class StatisticsType(str, Enum):
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"
    ALL = "all"


class Statistics(CallbackData, prefix="stats"):
    statistics_type: str
