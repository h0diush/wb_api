from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode

from config.settings.development import TELEGRAM_BOT_TOKEN
from .handlers import send_welcome, help_commands, new_product, \
    get_registration_user

bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

dp.register_message_handler(send_welcome, commands=['start'])
dp.register_message_handler(help_commands, commands=['help'])
dp.register_message_handler(new_product, commands=['new_product'])
dp.register_message_handler(get_registration_user, commands=['reg'])
