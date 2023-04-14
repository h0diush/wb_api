from aiogram import executor
from django.core.management.base import BaseCommand

from bot.config_bot import dp


async def on_startup(_):
    print('[-] Бот запущен')


class Command(BaseCommand):
    help = 'Runs the Telegram bot and the Django development server'

    def handle(self, *args, **options):
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# TODO два раза запускается бот
