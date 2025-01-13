from aiogram import Router

from apps.bot.callbacks.currency import Currency as CurrencyCallback
from apps.users.models import update_or_create_user

router = Router()

@router.callback_query(CurrencyCallback.filter())
async def set_currency(call: CurrencyCallback):
    user_id = call.message.chat.id
    currency = call.data.split(":")[1]
    await call.answer("Valyuta muvaffaqiyatli o'zgartirildi!")
    await call.message.answer("Valyuta muvaffaqiyatli o'zgartirildi!", reply_markup=None)
    await update_or_create_user(user_id, currency_type=currency)
