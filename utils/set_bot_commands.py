from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("parse_mode_html", "Показать пример HTML форматирования"),
    ])
