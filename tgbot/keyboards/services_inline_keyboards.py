from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot.keyboards.callback_data_factory import services_callback
from aiogram.types.web_app_info import WebAppInfo

"""Клавиатура список популярных услуг"""
services_markup = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚫Удаление тату!",
                callback_data=services_callback.new(
                    service_name="delete_tatu",
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="☄️Лазерное омоложение и шлифовка на PicoSure",
                callback_data=services_callback.new(
                    service_name="pico",
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="💎SMAS-лифтинг на аппарате Ulthera System",
                callback_data=services_callback.new(
                    service_name="ulthera",
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="🎇Фотоомоложение на аппарате BBL",
                callback_data=services_callback.new(
                    service_name="bbl",
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="🍀Лазерная эпиляция на аппарате Elite+",
                callback_data=services_callback.new(
                    service_name="elit_plus",
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="❄️Криолиполиз COCCON",
                callback_data=services_callback.new(
                    service_name="coccon",
                ),
            )
        ],
    ],
)

'''Клавиатура Удаление тату!"'''
service_tatu_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="ℹ️Подробнее",
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
        # [
        #     InlineKeyboardButton(
        #         text="📲Скачать приложение",
        #         web_app=WebAppInfo(url="https://xella.shop/"),
        #     )
        # ],
        [InlineKeyboardButton(text="↩️К списку услуг", callback_data="chanel_service")],
    ],
)

"""Клавиатура Лазерное омоложение и шлифовка на PicoSure"""
service_pico_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="ℹ️Подробнее об услуге",
                web_app=WebAppInfo(
                    url="https://xella.clinic/uslugi/apparat/picosureomolozhenie"
                ),
            ),
            InlineKeyboardButton(
                text="✅Записаться",
                web_app=WebAppInfo(
                    url="https://b157912.yclients.com/company/163813/menu?o="
                ),
            ),
        ],
        [InlineKeyboardButton(text="↩️К списку услуг", callback_data="chanel_service")],
    ],
)

'''Клавиатура SMAS-лифтинг на аппарате Ulthera System"'''
service_ultera_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="ℹ️Подробнее об услуге",
                web_app=WebAppInfo(url="https://xella.clinic/uslugi/apparat/ultherapy"),
            ),
            InlineKeyboardButton(
                text="✅Записаться",
                web_app=WebAppInfo(
                    url="https://b157912.yclients.com/company/163813/menu?o="
                ),
            ),
        ],
        [InlineKeyboardButton(text="↩️К списку услуг", callback_data="chanel_service")],
    ],
)

"""Клавиатура Фотоомоложение на аппарате BBL"""

service_bbl_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="ℹ️Подробнее об услуге",
                web_app=WebAppInfo(
                    url="https://xella.clinic/uslugi/apparat/bblomolozhenie"
                ),
            ),
            InlineKeyboardButton(
                text="✅Записаться",
                web_app=WebAppInfo(
                    url="https://b157912.yclients.com/company/163813/menu?o="
                ),
            ),
        ],
        [InlineKeyboardButton(text="↩️К списку услуг", callback_data="chanel_service")],
    ],
)


"""Клавиатура Лазерная эпиляция на аппарате Elite+"""

service_epil_keyboard = InlineKeyboardMarkup(
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
        [InlineKeyboardButton(text="↩️К списку услуг", callback_data="chanel_service")],
    ],
)


"""Клавиатура Криолиполиз COCCON"""

service_coccon_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="ℹ️Подробнее об услуге",
                web_app=WebAppInfo(
                    url="https://xella.clinic/uslugi/body/cryolipolysis"
                ),
            ),
            InlineKeyboardButton(
                text="✅Записаться",
                web_app=WebAppInfo(
                    url="https://b157912.yclients.com/company/163813/menu?o="
                ),
            ),
        ],
        [InlineKeyboardButton(text="↩️К списку услуг", callback_data="chanel_service")],
    ],
)
