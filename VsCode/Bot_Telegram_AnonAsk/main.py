import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
bot = Bot(token='7902582953:AAGHVc373Ii6NrpAFnx68VSpkp6XFR0CpXQ')
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await bot.send_message(message.chat.id, 'Hello')
    await message.answer('Hello Two')
    await message.reply('Reply Message')


dp.run_polling(bot)