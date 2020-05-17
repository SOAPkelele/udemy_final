from loader import bot, storage, db
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    print("Создаем таблицу пользователей")
    try:
        await db.create_table_users()
    except Exception as err:
        print(err)
    print("Готово")

    print("Чистим таблицу пользователей")
    await db.delete_users()
    print("Готово")
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
