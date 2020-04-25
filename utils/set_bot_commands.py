from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("callback", "Заказать обратный звонок"),
        types.BotCommand("show_on_map", "Показать ближайшие магазины"),
    ])
