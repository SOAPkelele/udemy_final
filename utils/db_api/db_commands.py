from typing import List

from sqlalchemy import and_

from utils.db_api.models import Item, User
from loader import db


async def add_user(user_id, full_name, username):
    try:
        return await User(user_id=int(user_id), name=full_name, username=username).create()
    except Exception:
        await select_user(int(user_id))


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(user_id: int):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.user_id).gino.scalar()
    return total


# Функция для создания нового товара в базе данных. Принимает все возможные аргументы, прописанные в Item
async def add_item(**kwargs):
    new_item = await Item(**kwargs).create()
    return new_item


# Функция для вывода товаров с РАЗНЫМИ категориями
async def get_categories() -> List[Item]:
    return await Item.query.distinct(Item.category_name).gino.all()


# Функция для вывода товаров с РАЗНЫМИ подкатегориями в выбранной категории
async def get_subcategories(category) -> List[Item]:
    return await Item.query.distinct(Item.subcategory_name).where(Item.category_code == category).gino.all()


# Функция для подсчета товаров с выбранными категориями и подкатегориями
async def count_items(category_code, subcategory_code=None):
    # Прописываем условия для вывода (категория товара равняется выбранной категории)
    conditions = [Item.category_code == category_code]

    # Если передали подкатегорию, то добавляем ее в условие
    if subcategory_code:
        conditions.append(Item.subcategory_code == subcategory_code)

    # Функция подсчета товаров с указанными условиями
    total = await db.select([db.func.count()]).where(
        and_(*conditions)
    ).gino.scalar()
    return total


# Функция вывода всех товаров, которые есть в переданных категории и подкатегории
async def get_items(category_code, subcategory_code) -> List[Item]:
    item = await Item.query.where(
        and_(Item.category_code == category_code,
             Item.subcategory_code == subcategory_code)
    ).gino.all()
    return item


# Функция для получения объекта товара по его айди
async def get_item(item_id) -> Item:
    item = await Item.query.where(Item.id == int(item_id)).gino.first()
    return item
