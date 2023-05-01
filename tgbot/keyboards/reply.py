from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧾Услуги'),
            KeyboardButton(text='✅Онлайн запись')
        ],
        [
            KeyboardButton(text='💫Акции'),
            KeyboardButton(text='🛍️XELLA shop'),
        ],
[
            KeyboardButton(text='🕐Режим работы'),
            KeyboardButton(text='📍Контакты'),
        ],
    ],
    resize_keyboard=True
)