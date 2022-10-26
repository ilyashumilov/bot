import os
import telebot
from markups import *
from messages import *

token  =  os.getenv('TOKEN')
bot=telebot.TeleBot (token)
@bot.message_handler(commands=['start'])
def start(message):
      bot.send_message(message.chat.id, msg1, reply_markup=markup1)
bot.polling(none_stop=True)
