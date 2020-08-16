from sqlalchemy import (Column, Integer, String, DateTime, BigInteger, ForeignKey, Boolean, Float)
from sqlalchemy.dialects.postgresql import JSON

from utils.db_api.database import db


class TimedBaseModel(db.Model):
    __abstract__ = True

    created_at = Column(DateTime(True), default=db.func.now())
    updated_at = Column(DateTime(True),
                        default=db.func.now(),
                        onupdate=db.func.now())


class User(TimedBaseModel):
    __tablename__ = "usersmanage_user"
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    user_id = Column(BigInteger, unique=True)

    name = Column(String(length=100))
    username = Column(String(length=100), nullable=True)
    email = Column(String(length=100), nullable=True)


class Referral(TimedBaseModel):
    __tablename__ = "usersmanage_referral"
    id = Column(ForeignKey("usersmanage_user.id", ondelete="CASCADE"), primary_key=True)
    referrer_id = Column(BigInteger)


class Item(TimedBaseModel):
    __tablename__ = "usersmanage_item"
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)

    name = Column(String(length=50))
    photo = Column(String(length=200))
    price = Column(Float)
    description = Column(String(length=3000), nullable=True)

    category_code = Column(String(20))
    category_name = Column(String(50))
    subcategory_code = Column(String(50))
    subcategory_name = Column(String(20))


class Purchase(TimedBaseModel):
    __tablename__ = "usersmanage_purchase"
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)

    buyer_id = Column(ForeignKey("usersmanage_user.id", ondelete="SET DEFAULT"), default=0)
    item_id_id = Column(ForeignKey("usersmanage_item.id", ondelete="CASCADE"))
    amount = Column(Float)
    quantity = Column(Integer)
    purchase_time = Column(DateTime, default=db.func.now())
    shipping_address = Column(JSON, nullable=True)
    phone_number = Column(String(50), nullable=True)
    email = Column(String(100), nullable=True)
    receiver = Column(String(100), nullable=True)
    successful = Column(Boolean, default=False)
