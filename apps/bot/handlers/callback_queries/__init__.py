from aiogram import Router

from .language import router as language_router
from .currency import router as currency_router
from .menu import router as menu_router

router = Router()
router.include_router(menu_router)
router.include_router(language_router)
router.include_router(currency_router)
