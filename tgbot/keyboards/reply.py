from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo


menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧾Услуги'),
            KeyboardButton(text='✅Онлайн запись', web_app=WebAppInfo(url='https://b157912.yclients.com/company/163813/menu?o='))
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