from aiogram import Dispatcher, types, Bot, executor

bot = Bot('')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    newlink = types.InlineKeyboardMarkup(row_width=3)
    newlink.add(types.InlineKeyboardButton('Моя ссылка', callback_data='mylink'))
    newlink.add(types.InlineKeyboardButton('Статистика', callback_data='statistik'))
    newlink.add(types.InlineKeyboardButton('Сохраненные ссылки', callback_data='savelink'))
    await bot.send_message(message.chat.id, 'Привет, это бот для анонимных сообщений\nДля начала тебе нужно создать свою ссылку', reply_markup=newlink)


@dp.callback_query_handler()
async def call(call):
    if call.data == 'mylink':
        

executor.start_polling(dp)
