from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧾Расскажи про услуги'),
            KeyboardButton(text='✅Хочу записаться со скидкой',
                           web_app=WebAppInfo(url='https://b157912.yclients.com/company/163813/menu?o='))
        ],
        [
            KeyboardButton(text='💫Расскажи про акции'),
            KeyboardButton(text='📱Расскажи о приложении XELLA', web_app=WebAppInfo(url='https://xella.shop/')),
        ],
        [
            KeyboardButton(text='❤️Расскажи о клинике'),
            KeyboardButton(text='📍Как вас найти?'),
        ],
    ],
    resize_keyboard=True
)
