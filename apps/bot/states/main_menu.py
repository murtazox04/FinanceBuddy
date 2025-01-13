from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):
    menu = State()
    add_category = State()


class AddExpense(StatesGroup):
    category = State()
    subcategory = State()
    amount = State()
    comment = State()
    date = State()
