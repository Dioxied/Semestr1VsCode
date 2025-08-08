import telebot
import sqlite3


bot = telebot.TeleBot('7589670050:AAHcpGg3qnNCyYUWEccZVtH7TSGWLLeFOHM')
name=None
link_SQL='./tbot/itproger.sql'

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect(link_SQL)
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50), id_user_tg varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    print(message.text)

    bot.send_message(message.chat.id, 'Hello, send your name: ')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Send your pass: ')
    bot.register_next_step_handler(message, user_pass)
def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect(link_SQL)
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass, id_user_tg) VALUES ("%s", "%s", "%s")' % (name, password, message.from_user.username))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('List Users', callback_data='user_list'))
    bot.send_message(message.chat.id, 'Users registration nice', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect(link_SQL)
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Name: {el[1]}, pass: {el[2]}, id: {el[3]}\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)