from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot.keyboards.callback_data_factory import stocks_callback
from aiogram.types.web_app_info import WebAppInfo

"""Клавиатура список акций"""
stocks_markup = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅Скидка 5% на онлайн запись!",
                callback_data=stocks_callback.new(
                    stock_name="online", stock_date="бессрочно"
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥Скидка 10% на первый сеанс удаления тату!",
                callback_data=stocks_callback.new(
                    stock_name="tatu", stock_date="до 01.08.2023"
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="💬Скидка 10% за отзыв на Яндекс.Картах!",
                callback_data=stocks_callback.new(
                    stock_name="feedback", stock_date="бессрочно"
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="🛍️Скидка 9% на покупки в XELLA shop!",
                callback_data=stocks_callback.new(
                    stock_name="shop", stock_date="до 10.06.2023"
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="☄️️Кешбэк 15% на лазерную эпиляцию",
                callback_data=stocks_callback.new(
                    stock_name="epil", stock_date="до 01.07.2023"
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="✨️Скидка 15% на перманентный макияж",
                callback_data=stocks_callback.new(
                    stock_name="pm", stock_date="до 01.07.2023"
                ),
            )
        ],
    ],
)

'''Клавиатура акции "онлайн записи"'''
stock_online_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="ℹ️Подробнее", web_app=WebAppInfo(url="https://xella.clinic/akcii")
            ),
            InlineKeyboardButton(
                text="✅Записаться",
                web_app=WebAppInfo(
                    url="https://b157912.yclients.com/company/163813/menu?o="
                ),
            ),
        ],
        [
            InlineKeyboardButton(
                text="📲Скачать приложение",
                web_app=WebAppInfo(url="https://xella.shop/"),
            )
        ],
        [InlineKeyboardButton(text="↩️К списку акций", callback_data="chanel")],
    ],
)

'''Клавиатура акции "скидка 10% на тату"'''
stock_tatu_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="ℹ️Подробнее об услуге",
                web_app=WebAppInfo(
                    url="https://xella.clinic/uslugi/tattoo/tattoo-removal"
                ),
            ),
            InlineKeyboardButton(
                text="✅Записаться",
                web_app=WebAppInfo(
                    url="https://b157912.yclients.com/company/163813/menu?o="
                ),
            ),
        ],
        [InlineKeyboardButton(text="↩️К списку акций", callback_data="chanel")],
    ],
)

'''Клавиатура акции "скидка за отзыв"'''
stock_feedback_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="ℹ️Подробнее об акции",
                web_app=WebAppInfo(url="https://xella.clinic/review/yandexmaps"),
            ),
            InlineKeyboardButton(
                text="💭Оставить отзыв",
                web_app=WebAppInfo(
                    url="https://yandex.ru/maps/org/klinika_esteticheskoy_meditsiny_xella/1134925283/reviews/?ll=37.627247%2C55.767271&z=17"
                ),
            ),
        ],
        [InlineKeyboardButton(text="↩️К списку акций", callback_data="chanel")],
    ],
)

"""Клавиатура акции скидка на покупки"""

shop_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📲Скачать приложение",
                web_app=WebAppInfo(url="https://xella.shop/"),
            )
        ],
        [InlineKeyboardButton(text="↩️К списку акций", callback_data="chanel")],
    ],
)


"""Клавиатура акции Кешбэк 15% на лазерную эпиляцию"""

epil_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="ℹ️Подробнее об услуге",
                web_app=WebAppInfo(url="https://xella.clinic/uslugi/epilation/laser"),
            ),
            InlineKeyboardButton(
                text="✅Записаться",
                web_app=WebAppInfo(
                    url="https://b157912.yclients.com/company/163813/menu?o="
                ),
            ),
        ],
        [InlineKeyboardButton(text="↩️К списку акций", callback_data="chanel")],
    ],
)


"""Клавиатура акции Скидка 15% на перманентный макияж"""

pm_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="ℹ️Подробнее об услуге",
                web_app=WebAppInfo(url="https://xella.clinic/uslugi/facecare"),
            ),
            InlineKeyboardButton(
                text="✅Записаться",
                web_app=WebAppInfo(
                    url="https://b157912.yclients.com/company/163813/menu?o="
                ),
            ),
        ],
        [InlineKeyboardButton(text="↩️К списку акций", callback_data="chanel")],
    ],
)
