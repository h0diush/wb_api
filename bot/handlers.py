from aiogram import types

from bot.messages.text import HELP_TEXT


async def send_welcome(message: types.Message):
    await message.answer("Привет! Я тестовый бот.")


async def help_commands(message: types.Message):
    await message.answer(HELP_TEXT)
