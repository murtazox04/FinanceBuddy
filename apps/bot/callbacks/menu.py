from typing import Optional
from enum import Enum
from aiogram.filters.callback_data import CallbackData


class ExpenceCategoryType(str, Enum):
    main_categories = "main"
    subcategories = "subcategories"
    search = "search"
    back = "back"
    add_category = "add_category"

class Expense(CallbackData, prefix="expence"):
    category_type: Optional[ExpenceCategoryType] = None
    category_id: Optional[int] = None
