from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Режим работы')
        ],
        [
            KeyboardButton(text='Контакты'),
            KeyboardButton(text='Услуги'),
        ],
    ],
    resize_keyboard=True
)