import datetime

from aiogram.types import Message
from gspread import service_account

from keyboards.inline.button_4 import table_url


# Функция проверки введенной пользователем даты
async def check_input_date(message: Message):
    data = message.text
    date_format = '%d.%m.%y'
    correct_date = False

    # Определяется, возможно ли перевести строку в дату с указанным форматом
    try:
        datetime.datetime.strptime(data, date_format)
        correct_date = True
    except Exception:
        await message.answer('Дата неверна')

    # Если удалось, то данная дата записывается в гугл таблицу. Пользователю приходит сообщение
    if correct_date:
        await message.answer('Дата верна')
        client = service_account(filename='bot1.json')
        table = client.open_by_url(table_url)
        worksheet = table.worksheet('Лист1')
        len_b = len(worksheet.col_values(col=2))
        worksheet.update(range_name=f'B{len_b + 1}', values=[[f'{data}']])

