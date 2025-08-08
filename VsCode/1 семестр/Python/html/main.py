import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('7805577831:AAEgieFeB0fVRqcZLPUVev1UOEU8YLV-E_Y')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Ежжи')
    btn2 = types.KeyboardButton('Удалить')
    btn3 = types.KeyboardButton('photo')
    markup.row(btn1)
    markup.row(btn2,btn3)
    bot.send_message(message.chat.id, 'Heelo', reply_markup=markup)
    file = open(r'D:\VsCode\Python\tbot\849339288083.mp4', 'rb')
    bot.send_video(message.chat.id, file)
    file = open(r'D:\VsCode\Python\tbot\audio.mp3', 'rb')
    bot.send_audio(message.chat.id, file)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Ежжи':
        bot.send_message(message.chat.id, 'Хуежжи, ты че еблан?')
    elif message.text == 'Удалить':
        bot.send_message(message.chat.id, "Себя удали, чмо")


@bot.message_handler(content_types=['photo'])
def photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Ежжи', url = 'https://vk.com')
    btn2 = types.InlineKeyboardButton('Удалить', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2,btn3)
    bot.reply_to(message, 'your proto', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_massage(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edited', callback.message.chat.id, callback.message.message_id)

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://vk.com')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'ХУЙ')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<strong>ПЕНИС</strong>', parse_mode='html')

@bot.message_handler(commands=['me'])
def main(message):
    bot.send_message(message.chat.id, message.chat.first_name)

@bot.message_handler()
def info(message):
    if message.text.lower()=='hi':
        bot.send_message(message.chat.id, 'Russia')
    elif message.text.lower()=='id':
        bot.reply_to(message, f'id : {message.text}')
    elif message.text.lower()=='photo':
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-entity_search/118114/922995041/S600xU_2x')





bot.polling(non_stop=True)