from aiogram.filters import StateFilter
from aiogram.types import Message

from loader import my_router


# Эхо-функция. При вводе каких-либо фраз вне установленных команд бот не молчит и отвечает
# пользователю его же сообщениями
@my_router.message(StateFilter(None))
async def bot_echo(message: Message):
    await message.reply(f'{message.text}')