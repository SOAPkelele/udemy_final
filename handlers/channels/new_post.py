from aiogram import types

from loader import dp, bot


@dp.channel_post_handler(content_types=types.ContentType.ANY)
async def new_post(message: types.Message):
    # Do something?
    pass
