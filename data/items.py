from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.item import Item

Tesla_S = Item(
    title="Tesla Model S",
    description="Tesla Model S — пятидверный электромобиль производства американской компании Tesla. "
                "Прототип был впервые показан на Франкфуртском автосалоне в 2009 году; "
                "поставки автомобиля в США начались в июне 2012 года",
    currency="UAH",
    prices=[
        LabeledPrice(
            label="Тесла Model S",
            amount=10_000_00
        )
    ],
    start_parameter="create_invoice_tesla_model_s",
    photo_url="https://www.ixbt.com/img/n1/news/2019/10/6/Model-S-hero-e1556066115259_large.jpg",
    photo_size=600
)

Tesla_X = Item(
    title="Tesla Model X",
    description="Tesla Model X — полноразмерный электрический кроссовер производства компании Tesla. "
                "Прототип был впервые показан в Лос-Анджелесе 9 февраля 2012 года. "
                "Коммерческие поставки начались 29 сентября 2015 года. "
                "Tesla Model X разрабатывается на базе платформы "
                "Tesla Model S и собирается на основном заводе компании во Фримонте, штат Калифорния.",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Tesla",
            amount=35_000_00
        ),
        LabeledPrice(
            label="Доставка",
            amount=15_000_00
        ),
        LabeledPrice(
            label="Скидка",
            amount=-5_000_00
        ),
        LabeledPrice(
            label="НДС",
            amount=10_000_00
        ),
    ],
    need_shipping_address=True,
    start_parameter="create_invoice_tesla_model_x",
    photo_url="https://www.tesla.com/sites/tesla/files/curatedmedia/performance-hero%402.jpg",
    photo_size=600,
    is_flexible=True
)

POST_REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title='Почтой',
    prices=[
        types.LabeledPrice(
            'Обычная коробка', 0),
        types.LabeledPrice(
            'Почтой обычной', 1000_00),
    ]
)
POST_FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Почтой (vip)',
    prices=[
        types.LabeledPrice(
            'Супер прочная коробка', 1000_00),
        types.LabeledPrice(
            'Почтой срочной - DHL (3 дня)', 3000_00),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title='Самовывоз',
                                       prices=[
                                           types.LabeledPrice('Самовывоз из магазина', -100_00)
                                       ])
