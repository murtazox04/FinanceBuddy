import json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from aiogram import Bot, Dispatcher
from aiogram.types import Update

from apps.bot.handlers.commands import router as commands_router
from apps.bot.handlers.callback_queries import router as callback_queries_router

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

dp.include_router(commands_router)
dp.include_router(callback_queries_router)


@csrf_exempt
async def telegram_webhook(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            update = Update(**json_data)
            await dp.feed_update(bot, update)
        except Exception as e:
            print(f"Error processing update: {e}")
        return JsonResponse({'status': 'OK'})
    else:
        return HttpResponse("Webhook endpoint.", status=200)
