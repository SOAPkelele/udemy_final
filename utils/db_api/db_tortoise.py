from tortoise import Tortoise
from tortoise import fields
from tortoise.models import Model

from data import config


class TimedBaseModel(Model):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


async def on_startup():
    print("Setup Connection")

    await Tortoise.init(
        db_url=config.POSTGRES_URI,
        modules={'models': ['utils.db_api.schemas']}
    )
    await Tortoise.generate_schemas()
