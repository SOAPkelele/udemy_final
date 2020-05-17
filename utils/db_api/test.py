import asyncio
import utils.db_api.quick_commands as commands
from utils.db_api.db_gino import db
from data import config

loop = asyncio.get_event_loop()


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

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


loop.run_until_complete(test())
