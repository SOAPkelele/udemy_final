from random import randint

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hcode
from blockcypher import from_satoshis

from data import config
from data.items import items
from keyboards.inline.purchases import buy_keyboard, paid_keyboard
from loader import dp
from utils.misc.bitcoin_payments import Payment, NotConfirmed, NoPaymentFound
from utils.misc.qr_code import qr_link


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    caption = """
Название продукта: {title}
<i>Описание:</i>
{description}

<u>Цена:</u> {price:.8f} <b>BTC</b>
"""

    for item in items:
        await message.answer_photo(
            photo=item.photo_link,
            caption=caption.format(
                title=item.title,
                description=item.description,
                price=item.price
            ),
            reply_markup=buy_keyboard(item_id=item.id)
        )


@dp.callback_query_handler(text_contains="buy")
async def create_invoice(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    item_id = call.data.split(":")[-1]
    item_id = int(item_id) - 1
    item = items[item_id]

    amount = item.price + randint(5, 500)
    payment = Payment(amount=amount)
    payment.create()

    show_amount = from_satoshis(payment.amount, "btc")
    await call.message.answer(f"Оплатите {show_amount:.8f} по адресу:\n\n" +
                              hcode(config.WALLET_BTC),
                              reply_markup=paid_keyboard)
    qr_code = config.REQUEST_LINK.format(address=config.WALLET_BTC,
                                         amount=show_amount,
                                         message="test")
    await call.message.answer_photo(photo=qr_link(qr_code))
    await state.set_state("btc")
    await state.update_data(payment=payment)


@dp.callback_query_handler(text="cancel", state="btc")
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Отменено")
    await state.finish()


@dp.callback_query_handler(text="paid", state="btc")
async def approve_payment(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment: Payment = data.get("payment")
    try:
        payment.check_payment()
    except NotConfirmed:
        await call.message.answer("Транзакция найдена. Но еще не подтверждена. Попробуйте позже")
        return
    except NoPaymentFound:
        await call.message.answer("Транзакция не найдена.")
        return
    else:
        await call.message.answer("Успешно оплачено")
    await call.message.delete_reply_markup()
    await state.finish()
