from aiogram.fsm.state import State, StatesGroup


# Стейт для связи отдельных функций между собой
class UserData(StatesGroup):
    date_from_user = State()
