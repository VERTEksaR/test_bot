from aiogram.filters import Command
from aiogram.types import Message

from loader import my_router


# Стартовая функция бота
@my_router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer(f'Привет, {message.from_user.username}')
