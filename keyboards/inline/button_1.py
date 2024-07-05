from aiogram.types import Message
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


url = 'https://yandex.ru/maps/2/saint-petersburg/house/ulitsa_lenina_1a/Z0kYdQ5oQUECQFtjfXRwcHRiYw==/?ll=30.401705%2C59.812708&z=14.95'


# Создание первой inline-кнопки с переходом на яндекс карту
async def yandex_map(message: Message) -> None:
    button = InlineKeyboardBuilder()

    btn1 = InlineKeyboardButton(text='Перейти в Яндекс Карты', url=url)
    button.add(btn1)
    await message.answer('Нажав на кнопку вы узнаете, где в СПБ дом 1 на улице Ленина',
                         reply_markup=button.as_markup())
