from aiogram import Dispatcher
from aiogram.types import Message
from tgbot.misc.throttling import rate_limit


@rate_limit(5)
async def user_start(message: Message):
    await message.reply("Привет я тестовый бот!")


async def open_command(message: Message):
    await message.answer('Режим работы:\n'
                         'Пн-Пт с 8:00 до 20:00')


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start", "help"], state="*")
    dp.register_message_handler(open_command, commands=['Режим_работы'])
