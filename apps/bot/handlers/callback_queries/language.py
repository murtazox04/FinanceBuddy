from aiogram import Router

from apps.bot.callbacks.language import Language as LangueCallback
from apps.users.models import update_or_create_user
from apps.bot.keyboards.inline import currency_keyboard

router = Router()


@router.callback_query(LangueCallback.filter())
async def set_language(call: LangueCallback):
    user_id = call.message.chat.id
    lang = call.data.split(":")[1]
    messages = {
        "uz": "Til muvaffaqiyatli o'zgartirildi! Valyutani tanlang.",
        "ru": "Язык успешно изменен! Выберите валюту.",
        "en": "Language successfully changed! Choose currency.",
        "uz_cyrl": "Тил муваффақиятли ўзгартирилди! Валютани танланг.",
    }
    text = messages.get(lang, "Language not supported.")  # Fallback for unsupported languages
    markup = currency_keyboard()
    await call.message.answer(text, reply_markup=markup)
    await call.answer(text.split("!")[0])  # Show notification for the first sentence
    await update_or_create_user(user_id, language_code=lang)
