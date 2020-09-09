from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from asgiref.sync import sync_to_async

from keyboards.inline.menu_keyboards import buy_item
from loader import dp
from utils.db_api.db_commands import select_user, get_item, add_item
from django_project.telegrambot.usersmanage.models import Purchase


@dp.callback_query_handler(buy_item.filter())
async def enter_buy(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    item_id = callback_data.get("item_id")
    user = await select_user(call.from_user.id)
    item = await get_item(item_id)

    purchase = Purchase()
    purchase.buyer_id = user.id
    purchase.item_id_id = int(item_id)
    purchase.receiver = call.from_user.full_name
    await state.update_data(purchase=purchase, item=item)

    await call.message.answer("Введите количество товара")
    await state.set_state("enter_quantity")


@dp.message_handler(state="enter_quantity")
async def enter_quantity(message: types.Message, state: FSMContext):
    quantity = message.text
    try:
        quantity = int(quantity)
    except ValueError:
        await message.answer("Неверное значение, введите заново")
        return
    async with state.proxy() as data:
        data["purchase"].quantity = quantity
        data["purchase"].amount = quantity * data["item"].price

    await message.answer("Пришлите свой телефон", reply_markup=ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton("Прислать", request_contact=True)
        ]], resize_keyboard=True
    ))
    await state.set_state("enter_phone")


@dp.message_handler(state="enter_phone", content_types=types.ContentType.CONTACT)
async def enter_phone(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    async with state.proxy() as data:
        data["purchase"].phone_number = phone_number
        await sync_to_async(data["purchase"].save)()
    await message.answer("Покупка создана")
    await state.finish()
