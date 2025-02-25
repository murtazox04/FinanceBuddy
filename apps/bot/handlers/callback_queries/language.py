from aiogram import Router, types
from apps.bot.callbacks.language import Language as LangueCallback
from apps.users.models import update_or_create_user
from apps.bot.keyboards.inline import currency_keyboard

router = Router()


@router.callback_query(LangueCallback.filter())
async def set_language(
    call: types.CallbackQuery, callback_data: LangueCallback
) -> None:
    user_id: int = call.message.chat.id
    lang: str = callback_data.language
    messages = {
        "uz": "Til muvaffaqiyatli o'zgartirildi! Valyutani tanlang.",
        "ru": "Язык успешно изменен! Выберите валюту.",
        "en": "Language successfully changed! Choose currency.",
        "uz_cyrl": "Тил муваффақиятли ўзгартирилди! Валютани танланг.",
    }
    text: str = messages.get(lang, "Language not supported.")
    markup = currency_keyboard()
    await call.message.answer(text, reply_markup=markup)
    await call.answer(text.split("!")[0])
    await update_or_create_user(user_id, language_code=lang)
