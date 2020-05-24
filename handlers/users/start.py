import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    non_existing_user = 666666
    non_existing_message_id = 666666

    try:
        await message.answer("Неправильно закрыт <b>тег<b>")
    except Exception as err:
        await message.answer(err)
    try:
        await message.answer("Не существует <kek>тега</kek>")
    except Exception as err:
        await message.answer(err)
    try:
        await bot.send_message(chat_id=non_existing_user, text="Не существующий пользователь")

    except Exception as err:
        await message.answer(err)

    logging.info("Пытаемся удалить сообщение")
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=non_existing_message_id)
    logging.info("Это не выполнится, но бот не упадет.")
