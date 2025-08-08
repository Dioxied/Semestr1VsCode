from aiogram import Bot, Dispatcher, types, executor
import asyncio

bot = Bot('7589670050:AAHcpGg3qnNCyYUWEccZVtH7TSGWLLeFOHM')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await bot.send_message(message.chat.id, 'Heelo')
    print(message)
    await message.answer('Hello')

    await message.reply('hi')

@dp.message_handler()
async def info(message: types.message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('site', url='vk.com'))
    markup.add(types.InlineKeyboardButton('hui', callback_data='chmo'))
    await message.reply('hernya', reply_markup=markup)    


@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)



async def main():
    await dp.start_polling(bot)


executor.start_polling(dp)