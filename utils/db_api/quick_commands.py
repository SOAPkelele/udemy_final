from asyncpg import UniqueViolationError

from utils.db_api.schemas.user import User
from utils.db_api.db_gino import db


async def add_user(id: int, name: str, email: str = None):
    try:
        return await User(id=id, name=name, email=email).create()
    except UniqueViolationError:
        pass


async def select_all_users():
    return await User.query.gino.all()


async def select_user(id):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_user_email(id, email):
    user = await User.get(id)
    await user.update(email=email).apply()


async def delete_users(self):
    await self.db.drop_all(tables="Users")
