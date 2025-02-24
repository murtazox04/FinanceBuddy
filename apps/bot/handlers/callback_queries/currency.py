from aiogram import Router, types

from apps.bot.callbacks.currency import Currency as CurrencyCallback
from apps.users.models import update_or_create_user

router = Router()


@router.callback_query(CurrencyCallback.filter())
async def set_currency(call: types.CallbackQuery, callback_data: CurrencyCallback):
    if call.message is None:
        await call.answer("Cannot process this callback: no message found")
        return
    user_id = call.message.chat.id
    if call.data:
        currency = callback_data.currency
    else:
        await call.answer("Invalid callback data")
        return
    try:
        await call.answer("Valyuta muvaffaqiyatli o'zgartirildi!")
        await call.message.answer("Valyuta muvaffaqiyatli o'zgartirildi!")
        await update_or_create_user(user_id, currency_type=currency)
    except Exception as e:
        print(f"Error in set_currency callback: {e}")
        await call.answer("An error occurred while processing your request.")
