from aiogram import F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import bot, my_router


# Функция создания inline-кнопки для показа картинки
async def image(message: Message) -> None:
    button = InlineKeyboardBuilder()

    btn1 = InlineKeyboardButton(text='Показать картинку', callback_data='btn1')
    button.add(btn1)
    await message.answer('Нажав эту кнопку в чат отправится красивая картинка',
                         reply_markup=button.as_markup())


# Удаления предыдущего сообщения с кнопкой и загрузка изображения в чат
@my_router.callback_query(F.data.in_('btn1',))
async def image_callback(callback: CallbackQuery) -> None:

    if callback.data == 'btn1':
        image_from_pc = FSInputFile('img1.jpg')
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.message.answer_photo(image_from_pc, caption='Изображение коровы')
