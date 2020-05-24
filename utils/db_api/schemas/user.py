from utils.db_api.db_tortoise import TimedBaseModel
from tortoise import fields


class User(TimedBaseModel):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, null=True)

    referral = fields.IntField(null=True)
