import os

from aiogram.types import Message
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv
from yoomoney import Quickpay


# Функция, создающая ссылку для оплаты
async def make_quick_pay_url(message: Message) -> str:
    load_dotenv()
    receiver = os.getenv('ACCOUNT_RECEIVER')
    quickpay = Quickpay(receiver=receiver, quickpay_form="shop",
                        targets="Sponsor this project",
                        paymentType="SB", sum=2, label=f"{message.from_user.id}")
    return quickpay.base_url


# Функция создания inline-кнопки для оплаты
async def p2p(message: Message) -> None:
    button = InlineKeyboardBuilder()

    url = await make_quick_pay_url(message)

    btn1 = InlineKeyboardButton(text='Оплатить p2p', url=url)
    button.add(btn1)
    await message.answer('Нажав эту кнопку вы будете перенаправлены на страницу оплаты',
                         reply_markup=button.as_markup())
