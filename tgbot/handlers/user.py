import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.callback_data_factory import stocks_callback
from tgbot.keyboards.inline import (
    stocks_markup,
    stock_online_keyboard,
    stock_tatu_keyboard,
    stock_feedback_keyboard,
    shop_keyboard,
    epil_keyboard,
)
from tgbot.misc.throttling import rate_limit
from tgbot.keyboards.reply import menu_ru
from aiogram.dispatcher.filters import Command, Text
from datetime import datetime

from tgbot.models.db_comands import select_all_stocks, get_name_stocks, select_stock

newdate = datetime.now()
now_date = newdate.strftime("%d.%m.%Y")


@rate_limit(5)
async def user_start(message: Message):
    await message.reply(
        f"Привет {message.from_user.first_name}, я тестовый бот клиники XELLA!\n\n"
        f"🟢Я расскажу тебе про акции которые проходят в нашей клинике.\n\n"
        f"🟢Помогу выбрать услугу и записаться на неё не выходя из телеграм.\n\n"
        f"🟢Расскажу где скачать и как пользоваться нашим мобильным приложением,\
                        в котором вы сможете не только записаться на любую услугу клиники,\
                         но и приобрести профессиональную косметику мировых брендов!\n\n"
        f"🟢Вы сможете узнать больше о нашей клинике, врачах и \
                        современном оборудовании которое мы используем.\n\n"
        f"🟢А в дальнейшем я смогу ответить на самые часто задаваемые\
                         вопросы или связать вас с администратором клиники.\n"
        f"О чем рассказать...?",
        reply_markup=menu_ru,
    )


@rate_limit(5)
async def open_command(message: Message):
    all_stocks = await get_name_stocks()
    for stock in all_stocks:
        await message.answer_photo(stock.image, caption=f"{stock.name}\n"
                                                        f"{stock.description}")


@rate_limit(5)
async def services(message: Message):
    await message.answer("А тут будет список услуг")


@rate_limit(5)
async def stocks(message: Message):
    await message.answer(f"Список акций на {now_date}:", reply_markup=stocks_markup)


@rate_limit(5)
async def contacts(message: Message):
    await message.answer(
        "А тут вы сможете узнать наши контактные данные,\
     перейти на наши каналы в социальных сетях или вызвать такси до клиники!"
    )


"""Обработка кнопок акций"""


@rate_limit(5)
async def online_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    stock_date = callback_data.get("stock_date")
    stock = await select_stock(1)
    await call.message.answer_photo(stock.image,
                                    caption=f"Акция действует {stock_date}!\n"
                                            f"{stock.name}\n"
                                            f"{stock.description}",
                                    reply_markup=stock_online_keyboard,
                                    )


@rate_limit(5)
async def tatu_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    stock_date = callback_data.get("stock_date")
    stock = await select_stock(2)
    await call.message.answer_photo(stock.image,
                                    caption=f"Акция действует {stock_date}!\n"
                                            f"{stock.name}\n"
                                            f"{stock.description}",
                                    reply_markup=stock_online_keyboard,
                                    )


@rate_limit(5)
async def feedback_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    stock_date = callback_data.get("stock_date")
    stock = await select_stock(3)
    await call.message.answer_photo(stock.image,
                                    caption=f"Акция действует {stock_date}!\n"
                                            f"{stock.name}\n"
                                            f"{stock.description}",
                                    reply_markup=stock_online_keyboard,
                                    )


@rate_limit(5)
async def chanel_btn(call: CallbackQuery):
    await call.answer("Список акций:")
    await call.message.edit_reply_markup(reply_markup=stocks_markup)


@rate_limit(5)
async def shop_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    stock_date = callback_data.get("stock_date")
    stock = await select_stock(4)
    await call.message.answer_photo(stock.image,
                                    caption=f"Акция действует {stock_date}!\n"
                                            f"{stock.name}\n"
                                            f"{stock.description}",
                                    reply_markup=stock_online_keyboard,
                                    )


@rate_limit(5)
async def epil_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    stock_date = callback_data.get("stock_date")
    stock = await select_stock(5)
    await call.message.answer_photo(stock.image,
                                    caption=f"Акция действует {stock_date}!\n"
                                            f"{stock.name}\n"
                                            f"{stock.description}",
                                    reply_markup=stock_online_keyboard,
                                    )


@rate_limit(5)
async def pm_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    stock_date = callback_data.get("stock_date")
    stock = await select_stock(6)
    await call.message.answer_photo(stock.image,
                                    caption=f"Акция действует {stock_date}!\n"
                                            f"{stock.name}\n"
                                            f"{stock.description}",
                                    reply_markup=stock_online_keyboard,
                                    )


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start", "help"], state="*")
    dp.register_message_handler(open_command, Text(endswith="клинике"))
    dp.register_message_handler(services, Text(endswith="услуги"))

    dp.register_message_handler(stocks, Text(endswith="акции"))

    dp.register_message_handler(contacts, Text(endswith="найти?"))

    dp.register_callback_query_handler(
        online_btn, stocks_callback.filter(stock_name="online")
    )
    dp.register_callback_query_handler(
        tatu_btn, stocks_callback.filter(stock_name="tatu")
    )
    dp.register_callback_query_handler(
        feedback_btn, stocks_callback.filter(stock_name="feedback")
    )
    dp.register_callback_query_handler(
        shop_btn, stocks_callback.filter(stock_name="shop")
    )
    dp.register_callback_query_handler(
        epil_btn, stocks_callback.filter(stock_name="epil")
    )
    dp.register_callback_query_handler(pm_btn, stocks_callback.filter(stock_name="pm"))
    dp.register_callback_query_handler(chanel_btn, text="chanel")
