from aiogram import types

from bot.messages.text import HELP_TEXT
from .views import create_telegram_user


async def send_welcome(message: types.Message) -> None:
    await message.answer("Привет! Я тестовый бот.")


async def help_commands(message: types.Message) -> None:
    await message.answer(HELP_TEXT)


async def new_product(message: types.Message) -> None:
    args = message.get_args()
    if args:
        await message.answer(f'This is {args}')
    await message.answer('No args')


async def get_registration_user(message: types.Message):
    code = message.get_args()
    if not await create_telegram_user(code, message.from_user.id):
        return await message.answer('Проверьте введенный Вами код')
    return await message.answer('YES')
