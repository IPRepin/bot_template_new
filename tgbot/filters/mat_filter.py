from aiogram import Dispatcher
from aiogram.types import Message

import json, string


async def cenz(message: Message):
    if {
        i.lower().translate(str.maketrans("", "", string.punctuation))
        for i in message.text.split(" ")
    }.intersection(set(json.load(open("tgbot/filters/cenz.json")))) != set():
        await message.reply("🤬Маты запрещены")
        await message.delete()


def register_cenz(dp: Dispatcher):
    dp.register_message_handler(cenz)
