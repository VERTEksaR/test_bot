from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from gspread import service_account

from loader import bot, my_router

table_url = 'https://docs.google.com/spreadsheets/d/1YMGq3h-zT7ENPRs5ZDXLHEQ11kMxANHOV5WZl5j2AsM'


# Функция для ознакомления с данными, находящимися в определенной ячейке гугл талицы
async def google_sheet(message: Message) -> None:
    button = InlineKeyboardBuilder()

    btn1 = InlineKeyboardButton(text='A2', callback_data='A2')
    button.add(btn1)
    await message.answer('Нажмите на кнопку, чтобы узнать, что записано в'
                         'ячейке A2 в таблице "гугл_табличка"',
                         reply_markup=button.as_markup())


# Замена сообщения на результат поиска в таблице - значение ячейки
@my_router.callback_query(F.data.in_('A2',))
async def image_callback(callback: CallbackQuery) -> None:
    # Создаем клиент, используя настройки сервисного аккаунта гугл
    client = service_account(filename='bot1.json')
    # Заходим на нужную гугл таблицу по url
    table = client.open_by_url(table_url)
    # Выбираем нужный лист таблицы
    worksheet = table.worksheet('Лист1')
    # Берем информацию о нужной ячейке
    a2_data = worksheet.get('A2')[0][0]
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                text=f'В таблице "гугл табличка" в ячейке А2 написано: "{a2_data}"')
