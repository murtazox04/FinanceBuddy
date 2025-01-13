from aiogram import Router

from .start import router as start_router
from .help import router as help_router
from .view_stats import router as view_stats_router
from .delete_expense import router as delete_expense_router
from .export_data import router as export_data_router
from .feedback import router as feedback_router
from .notifications import router as notifications_router


router = Router()
router.include_router(start_router)
router.include_router(help_router)
router.include_router(view_stats_router)
router.include_router(delete_expense_router)
router.include_router(export_data_router)
router.include_router(feedback_router)
router.include_router(notifications_router)
