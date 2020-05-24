import asyncio

import utils.db_api.quick_commands as commands
from utils.db_api.db_tortoise import on_startup

loop = asyncio.get_event_loop()


async def test():
    await on_startup()

    print("Чистим таблицы")
    await commands.clean_tables()

    print("Добавляем пользователей")
    await commands.add_user(1, "One", "email")
    await commands.add_user(2, "Vasya", "vv@gmail.com")
    await commands.add_user(3, "1", "1")
    await commands.add_user(4, "1", "1")
    await commands.add_user(5, "John", "john@mail.com")
    print("Готово")

    users = await commands.select_all_users()
    print(f"Получил всех пользователей: {users}")

    user = await commands.select_user(id=5)
    print(f"Получил пользователя: {user}")

    print("Чистим таблицы")
    await commands.clean_tables()

    print("Тест успешный")


loop.run_until_complete(test())
