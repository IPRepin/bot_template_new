import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.callback_data_factory import stocks_callback
from tgbot.keyboards.inline import stocks_markup, stock_online_keyboard, stock_tatu_keyboard, stock_feedback_keyboard
from tgbot.misc.throttling import rate_limit
from tgbot.keyboards.reply import menu_ru
from aiogram.dispatcher.filters import Command, Text
from datetime import datetime


newdate = datetime.now()
now_date = newdate.strftime("%d.%m.%Y")


@rate_limit(5)
async def user_start(message: Message):
    await message.reply(f"Привет {message.from_user.first_name}, я тестовый бот клиники XELLA!\n\n"
                        f"🟢Я расскажу тебе про акции которые проходят в нашей клинике.\n\n"
                        f"🟢Помогу выбрать услугу и записаться на неё не выходя из телеграм.\n\n"
                        f"🟢Расскажу где скачать и как пользоваться нашим мобильным приложением,\
                        в котором вы сможете не только записаться на любую услугу клиники,\
                         но и приобрести профессиональную косметику мировых брендов!", reply_markup=menu_ru)


@rate_limit(5)
async def open_command(message: Message):
    await message.answer('Режим работы:\n'
                         'Пн-Пт с 8:00 до 20:00')
    # await message.delete()


@rate_limit(5)
async def services(message: Message):
    await message.answer('Список услуг:')
    # await message.delete()


# @rate_limit(5)
# async def online_recording(message: Message):
#     await message.answer('<a href="https://b157912.yclients.com/company/163813/menu?o="> 👉Записаться👈</a>')
    # await message.delete()


@rate_limit(5)
async def stocks(message: Message):
    await message.answer(f'Список акций на {now_date}', reply_markup=stocks_markup)
    # await message.delete()


@rate_limit(5)
async def shop(message: Message):
    await message.answer('Переход в магазин косметики')
    # await message.delete()


@rate_limit(5)
async def contacts(message: Message):
    await message.answer('Контактные данные')
    # await message.delete()


'''Обработка кнопок акций'''


@rate_limit(5)
async def online_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    stock_date = callback_data.get('stock_date')
    await call.message.answer(f"Акция действует {stock_date}!\n"
                              f"Записывайтесь самостоятельно через виджет онлайн-записи\
                               или мобильное приложение, а с нас скидка 5% на все",
                              reply_markup=stock_online_keyboard
                              )


@rate_limit(5)
async def tatu_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    stock_date = callback_data.get('stock_date')
    await call.message.answer(f"Акция действует {stock_date}! \n"
                              f"Если вы впервые удаляете тату, то получите скидку 10%\
                               на первый сеанс удаления на аппарате PicoSure",
                              reply_markup=stock_tatu_keyboard
                              )


@rate_limit(5)
async def feedback_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    stock_date = callback_data.get('stock_date')
    await call.message.answer(f"Акция действует {stock_date}! \n"
                              f"Всего 3 шага до получения скидки:\n"
                              f"1️⃣<b>Оставьте отзыв</b>\n"
                              f"Напишите, что вы думаете о нашей работе на Яндекс.Картах\n"
                              f"\n"
                              f"2️⃣<b>Подтвердите отзыв</b>\n"
                              f"Отправьте скриншот отзыва нам в WhatsApp или покажите на ресепшн при расчете\n"
                              f"\n"
                              f"3️⃣<b>Получите скидку</b>\n"
                              f"Мы сразу применим скидку к ближайшему визиту",
                              reply_markup=stock_feedback_keyboard,
                              )


@rate_limit(5)
async def chanel_btn(call: CallbackQuery):
    await call.answer("Список акций:")
    await call.message.edit_reply_markup(reply_markup=stocks_markup)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start", "help"], state="*")
    dp.register_message_handler(open_command, Text(endswith='работы'))
    dp.register_message_handler(services, Text(endswith='Услуги'))
    # dp.register_message_handler(online_recording, Text(endswith='запись'))
    dp.register_message_handler(stocks, Text(endswith='Акции'))
    dp.register_message_handler(shop, Text(endswith='shop'))
    dp.register_message_handler(contacts, Text(endswith='Контакты'))

    dp.register_callback_query_handler(online_btn, stocks_callback.filter(stock_name='online'))
    dp.register_callback_query_handler(tatu_btn, stocks_callback.filter(stock_name='tatu'))
    dp.register_callback_query_handler(feedback_btn, stocks_callback.filter(stock_name='feedback'))
    dp.register_callback_query_handler(chanel_btn, text='chanel')
