import os
from dotenv import load_dotenv, find_dotenv

# Проверка наличия файла .env
if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
# Создания кортежа с командами для работы с ботом в чате
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("button1", "Переход на Яндекс карты"),
    ("button2", "Оплата p2p"),
    ("button3", "Отправка изображения"),
    ("button4", "Получение значения значения из гугл таблицы"),
    ("write_date", "Записать дату в гугл таблицу")
)
