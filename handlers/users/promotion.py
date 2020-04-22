from aiogram.dispatcher.filters import Command

from loader import bot, dp


@dp.message_handler(Command("channels"))
