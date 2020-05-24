from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api.user import User
from utils.misc import rate_limit


# Можно запускать раз в 10 сек
@rate_limit(limit=10)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, user: User):
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Юзер полученный через миддлварь: {user.__dict__}')
