from aiogram import Bot, Dispatcher, types, executor
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import string
import sqlite3

async def indvKod():
    s=string.ascii_lowercase + string.digits + string.ascii_uppercase
    passw=''
    conn = sqlite3.connect(link_SQL)
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    while True:
        for i in range(5):
            passw += random.choice(s)
        for el in users:
            if el[3] == passw:
                break
        else:
            break

    conn.commit()
    cur.close()
    conn.close()
    return passw

class RegistrationStates(StatesGroup):
    start = State()
    startCode = State()
    glav_menu = State()
    waiting_for_email = State()

bot = Bot('7902582953:AAGHVc373Ii6NrpAFnx68VSpkp6XFR0CpXQ')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
link_SQL='/itproger.sql'

@dp.message_handler(commands=['start'])
async def start(message: types.message):
    if message.text == '/start':
        print(message)
        await RegistrationStates.start.set()
    else:
        await RegistrationStates.startCode.set()

@dp.message_handler(state=RegistrationStates.start)
async def startCh(message: types.message):
    conn = sqlite3.connect(link_SQL)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, chatId varchar(50), userName varchar(50), indvCode varchar(50))')
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    for el in users:
        if message.chat.username == el[2]:
            break
    else:
        cur.execute('INSERT INTO users (chatId, userName, indvCode) VALUES ("%s", "%s", "%s")' % (message.chat.id, message.chat.username, ''))


    conn.commit()
    cur.close()
    conn.close()
    create_link = types.InlineKeyboardMarkup()
    create_link.add(types.InlineKeyboardButton('Создать ссылку', callback_data= 'createLink'))
    await bot.send_message(message.chat.id, 'Привет, это бот для Анонимных сообщений😍\nЧтобы тебе смогли написать твои друзья, ты должен создать свою ссылку👍', reply_markup=create_link)
    
@dp.message_handler(state=RegistrationStates.startCode)
async def startCode(message: types.message):
    pass

@dp.callback_query_handler()
async def callback(call):
    if call.data == 'createLink':
        indvKod = indvKod()
        bot.send_message(call.message.chat.id, f'Твоя ссылка для анонимных сообщений: https://t.me/AnonAskTYS_bot?start={indvKod}')
        conn = sqlite3.connect(link_SQL)
        cur = conn.cursor() 
        cursor.execute('UPDATE Users SET indvCode = ? WHERE userName = ?', (indvKod, call.message.chat.username))
        conn.commit()
        cur.close()
        conn.close()


executor.start_polling(dp)