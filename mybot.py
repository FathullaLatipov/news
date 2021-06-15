import telebot
import requests
from telebot import types

bot = telebot.TeleBot('1738059418:AAHz2uV-qPNMJuP4DDG0iftFuRvDmSGFd1A')


def get_products_list(message):
    data = requests.get(f'http://localhost:9000/api/news/').json()
    data = data['results']
    result = ''
    for i in data:
        result += f"{i['id']}. {i['title']}\n"

    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3)
    keyboard.add(types.KeyboardButton('Посмотреть все новости'))
    keyboard.add(types.KeyboardButton('Посмотреть новости по ID'))

    bot.send_message(message.chat.id, 'Выбирите', reply_markup=keyboard)

    bot.register_next_step_handler(message, get_products_list)


bot.polling()
