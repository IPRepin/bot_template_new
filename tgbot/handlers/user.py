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
from tgbot.keyboards.services_inline_keyboards import (
    services_callback,
    service_epil_keyboard,
    service_coccon_keyboard,
    service_bbl_keyboard,
    service_pico_keyboard,
    service_tatu_keyboard,
    service_ultera_keyboard,
    services_markup,
)
from tgbot.misc.throttling import rate_limit
from tgbot.keyboards.reply import menu_ru
from aiogram.dispatcher.filters import Command, Text
from datetime import datetime

from tgbot.models.db_comands import (
    select_stock,
    select_service,
)

new_date = datetime.now()
now_date = new_date.strftime("%d.%m.%Y")


@rate_limit(5)
async def user_start(message: Message):
    await message.answer_photo(open('/home/pavelrepin/GitHub/bot_template_new/image/bot.png', 'rb'),caption=f"Привет {message.from_user.first_name}, я тестовый бот клиники XELLA!\n\n"
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
    await message.answer(
        "💞Xella — это клиника, создатели которой разделяют древнюю японскую философию Кинцуги🎌. \
        Мастера техники Кинцуги при помощи лака, где растворяют порошок золота или платины, \
        ювелирно восстанавливают разбитую керамику и превращают ее в произведение искусства. \
        Терпение, навык, опыт, качество и умение видеть красоту в изъянах стали основой вселенной Xella.\n"
        "\n"
        "👩‍⚕️Здесь вас встретят специалисты с высшим медицинским образованием, постоянно \
        обновляющие свои знания. Основатели Xella сравнивают поиск новых членов команды \
        с нырянием за жемчугом — настолько кропотливый поиск и тщательный отбор подразумевает\
         этот процесс. Все, кто работает для Xella, уверены, что красота — в балансе между\
          здоровьем и эстетикой. Каждый сотрудник разделяет доказательный подход к эстетической\
           медицине, а вся работа осуществляется только на лучших сертифицированных аппаратах \
           и с применением лицензированных средств.\n"
        "\n"
        "🔆Но главное, Xella — это коммьюнити единомышленников. Клиентов и друзей нашего\
         пространства объединяет стремление к самосовершенствованию, которое опирается на\
          любовь к себе, а не на ненависть к изъянам. В атмосфере поддержки и бережного\
           отношения друг к другу сообщество Xella размышляет о том, что такое красота — внешняя\
            и внутренняя, из чего она складывается, как эстетика становится стилем жизни и\
             способом смотреть на себя и на мир вокруг нас.\n"
        "🏵Добро пожаловать.🏵"
    )


@rate_limit(5)
async def services(message: Message):
    await message.answer(
        "Это список самых востребованных услуг нашей клиники:",
        reply_markup=services_markup,
    )


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
    await call.message.answer_photo(
        stock.image,
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
    await call.message.answer_photo(
        stock.image,
        caption=f"Акция действует {stock_date}!\n"
        f"{stock.name}\n"
        f"{stock.description}",
        reply_markup=stock_tatu_keyboard,
    )


@rate_limit(5)
async def feedback_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    stock_date = callback_data.get("stock_date")
    stock = await select_stock(3)
    await call.message.answer_photo(
        stock.image,
        caption=f"Акция действует {stock_date}!\n"
        f"{stock.name}\n"
        f"{stock.description}",
        reply_markup=stock_feedback_keyboard,
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
    await call.message.answer_photo(
        stock.image,
        caption=f"Акция действует {stock_date}!\n"
        f"{stock.name}\n"
        f"{stock.description}",
        reply_markup=shop_keyboard,
    )


@rate_limit(5)
async def epil_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    stock_date = callback_data.get("stock_date")
    stock = await select_stock(5)
    await call.message.answer_photo(
        stock.image,
        caption=f"Акция действует {stock_date}!\n"
        f"{stock.name}\n"
        f"{stock.description}",
        reply_markup=epil_keyboard,
    )


@rate_limit(5)
async def pm_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    stock_date = callback_data.get("stock_date")
    stock = await select_stock(6)
    await call.message.answer_photo(
        stock.image,
        caption=f"Акция действует {stock_date}!\n"
        f"{stock.name}\n"
        f"{stock.description}",
        reply_markup=stock_online_keyboard,
    )


"""Обработка кнопок услуг"""


@rate_limit(5)
async def delete_tatu_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    service = await select_service(1)
    await call.message.answer_photo(
        service.image,
        caption=f"{service.name}\n" f"{service.description}",
        reply_markup=service_tatu_keyboard,
    )


@rate_limit(5)
async def picosure_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    service = await select_service(2)
    await call.message.answer_photo(
        service.image,
        caption=f"{service.name}\n" f"{service.description}",
        reply_markup=service_pico_keyboard,
    )


@rate_limit(5)
async def ulthera_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    service = await select_service(3)
    await call.message.answer_photo(
        service.image,
        caption=f"{service.name}\n" f"{service.description}",
        reply_markup=service_ultera_keyboard,
    )


@rate_limit(5)
async def bbl_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    service = await select_service(4)
    await call.message.answer_photo(
        service.image,
        caption=f"{service.name}\n" f"{service.description}",
        reply_markup=service_bbl_keyboard,
    )


@rate_limit(5)
async def elit_plus_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    service = await select_service(5)
    await call.message.answer_photo(
        service.image,
        caption=f"{service.name}\n" f"{service.description}",
        reply_markup=service_epil_keyboard,
    )


@rate_limit(5)
async def coccon_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    service = await select_service(6)
    await call.message.answer_photo(
        service.image,
        caption=f"{service.name}\n" f"{service.description}",
        reply_markup=service_coccon_keyboard,
    )


@rate_limit(5)
async def chanel_service_btn(call: CallbackQuery):
    await call.answer("Список услуг:")
    await call.message.edit_reply_markup(reply_markup=services_markup)


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
    dp.register_callback_query_handler(
        delete_tatu_btn, services_callback.filter(service_name="delete_tatu")
    )
    dp.register_callback_query_handler(
        picosure_btn, services_callback.filter(service_name="pico")
    )
    dp.register_callback_query_handler(
        ulthera_btn, services_callback.filter(service_name="ulthera")
    )
    dp.register_callback_query_handler(
        bbl_btn, services_callback.filter(service_name="bbl")
    )
    dp.register_callback_query_handler(
        elit_plus_btn, services_callback.filter(service_name="elit_plus")
    )
    dp.register_callback_query_handler(
        coccon_btn, services_callback.filter(service_name="coccon")
    )
    dp.register_callback_query_handler(chanel_service_btn, text="chanel_service")
