from tortoise.exceptions import IntegrityError

from utils.db_api.schemas.user import User


async def add_user(id: int, name: str, email: str = None):
    try:
        return await User.create(id=id, name=name, email=email)
    except IntegrityError:
        pass


async def select_all_users():
    return await User.all().values()


async def select_user(id):
    user = await User.get_or_none(id=id).values()
    return user[0]


async def count_users():
    total = await User.all().count()
    return total


async def update_user_email(id, email):
    await User.filter(id=id).update(email=email)


async def clean_tables():
    await User.all().delete()
