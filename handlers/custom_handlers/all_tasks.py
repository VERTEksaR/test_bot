from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.data import UserData
from loader import my_router
from keyboards.inline import button_1, button_2, button_3, button_4
from utils.misc import check_input_date


# Реализовали отклик бота на команду /button1
@my_router.message(Command(commands=['button1']))
async def yandex_map(message: Message) -> None:
    await button_1.yandex_map(message)


# Реализовали отклик бота на команду /button2
@my_router.message(Command(commands=['button2']))
async def p2p(message: Message) -> None:
    await button_2.p2p(message)


# Реализовали отклик бота на команду /button3
@my_router.message(Command(commands=['button3']))
async def image(message: Message) -> None:
    await button_3.image(message)


# Реализовали отклик бота на команду /button4
@my_router.message(Command(commands=['button4']))
async def a2_data(message: Message) -> None:
    await button_4.google_sheet(message)


# Бот просит пользователя ввести дату
@my_router.message(Command(commands=['write_date']))
async def set_date(message: Message, state: FSMContext) -> None:
    await message.answer('Напишите дату')
    await state.set_state(UserData.date_from_user)


# Бот проверяет дату на валидность и если все хорошо - добавляет ее в гугл таблицу
@my_router.message(StateFilter(UserData.date_from_user))
async def check_date(message: Message) -> None:
    await check_input_date.check_input_date(message)
