import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.callback_data_factory import stocks_callback
from tgbot.keyboards.inline import stocks_markup, stock_online_keyboard, stock_tatu_keyboard, stock_feedback_keyboard, \
    shop_keyboard, epil_keyboard
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
                         но и приобрести профессиональную косметику мировых брендов!\n\n"
                        f"🟢Вы сможете узнать больше о нашей клинике, врачах и \
                        современном оборудовании которое мы используем.\n\n"
                        f"🟢А в дальнейшем я смогу ответить на самые часто задаваемые\
                         вопросы или связать вас с администратором клиники.\n"
                        f"О чем рассказать...", reply_markup=menu_ru)


@rate_limit(5)
async def open_command(message: Message):
    db = message.bot['db']
    stcs = await db.select_all_stocks()
    stock_data = list(stcs)
    stock_data_dict = dict(stock_data)

    stock_name = stock_data_dict.get('stock_name')
    await message.answer(f'Stock {stock_name}')

    # await message.delete()


@rate_limit(5)
async def services(message: Message):
    await message.answer('А тут будет список услуг')
    # await message.delete()


# @rate_limit(5)
# async def online_recording(message: Message):
#     await message.answer('<a href="https://b157912.yclients.com/company/163813/menu?o="> 👉Записаться👈</a>')
# await message.delete()


@rate_limit(5)
async def stocks(message: Message):
    await message.answer(f'Список акций на {now_date}:', reply_markup=stocks_markup)
    # await message.delete()


# @rate_limit(5)
# async def shop(message: Message):
#     await message.answer('Переход в магазин косметики')
    # await message.delete()


@rate_limit(5)
async def contacts(message: Message):
    await message.answer('А тут вы сможете узнать наши контактные данные,\
     перейти на наши каналы в социальных сетях или вызвать такси до клиники!')
    # await message.delete()


'''Обработка кнопок акций'''


@rate_limit(5)
async def online_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    stock_date = callback_data.get('stock_date')
    await call.message.answer_photo(open('tgbot/handlers/stocks_img/online.png', 'rb'),
                                    caption=f"Акция действует {stock_date}!\n"
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
    await call.message.answer_photo(open('tgbot/handlers/stocks_img/tatu.png', 'rb'),
                                    caption=f"Акция действует {stock_date}! \n"
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
    await call.message.answer_photo(open('tgbot/handlers/stocks_img/send.png', 'rb'),
                                    caption=f"Акция действует {stock_date}! \n"
                                            f"Всего 3 шага до получения скидки:\n"
                                            f"1️⃣<b>Оставьте отзыв</b>\n"
                                            f"Напишите, что вы думаете о нашей работе на Яндекс.Картах\n"
                                            f"\n"
                                            f"2️⃣<b>Подтвердите отзыв</b>\n"
                                            f"Отправьте скриншот отзыва нам в WhatsApp или покажите \
                                            на ресепшн при расчете\n"
                                            f"\n"
                                            f"3️⃣<b>Получите скидку</b>\n"
                                            f"Мы сразу применим скидку к ближайшему визиту",
                                    reply_markup=stock_feedback_keyboard,
                                    )


@rate_limit(5)
async def chanel_btn(call: CallbackQuery):
    await call.answer("Список акций:")
    await call.message.edit_reply_markup(reply_markup=stocks_markup)


@rate_limit(5)
async def shop_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    stock_date = callback_data.get('stock_date')
    await call.message.answer_photo(open('tgbot/handlers/stocks_img/shop.png', 'rb'),
                                    caption=f"Акция действует {stock_date}! \n"
                                            f"Скидка 9% на любые покупки в приложении XELLA по промокоду:\n"
                                            f"<code>MAYDAY</code>\n"
                                            f"на покупки от 3000₽",
                                    reply_markup=shop_keyboard
                                    )


@rate_limit(5)
async def epil_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    stock_date = callback_data.get('stock_date')
    await call.message.answer_photo(open('tgbot/handlers/stocks_img/epil.png', 'rb'),
                                    caption=f"Акция действует {stock_date}! \n"
                                            f"Мало, кто знает, что у нас есть один из лучших \
                                            александритовых аппаратов для лазерной эпиляции CynoSure Elite+",
                                    reply_markup=epil_keyboard
                                    )


@rate_limit(5)
async def pm_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    stock_date = callback_data.get('stock_date')
    await call.message.answer_photo(open('tgbot/handlers/stocks_img/pm.png', 'rb'),
                                    caption=f"Акция действует {stock_date}! \n"
                                            f"Отличный способ зафиксировать свою красоту на длительное\
                                             время у мастера ТОП-уровня, еще и со скидкой 15%",
                                    reply_markup=epil_keyboard
                                    )


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start", "help"], state="*")
    dp.register_message_handler(open_command, Text(endswith='клинике'))
    dp.register_message_handler(services, Text(endswith='услуги'))
    # dp.register_message_handler(online_recording, Text(endswith='запись'))
    dp.register_message_handler(stocks, Text(endswith='акции'))
    # dp.register_message_handler(shop, Text(endswith='shop'))
    dp.register_message_handler(contacts, Text(endswith='найти?'))

    dp.register_callback_query_handler(online_btn, stocks_callback.filter(stock_name='online'))
    dp.register_callback_query_handler(tatu_btn, stocks_callback.filter(stock_name='tatu'))
    dp.register_callback_query_handler(feedback_btn, stocks_callback.filter(stock_name='feedback'))
    dp.register_callback_query_handler(shop_btn, stocks_callback.filter(stock_name='shop'))
    dp.register_callback_query_handler(epil_btn, stocks_callback.filter(stock_name='epil'))
    dp.register_callback_query_handler(pm_btn, stocks_callback.filter(stock_name='pm'))
    dp.register_callback_query_handler(chanel_btn, text='chanel')
