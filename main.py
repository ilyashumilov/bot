import os
import telebot
from messages import *

token  =  os.getenv('TOKEN')

print(token)

bot=telebot.TeleBot (token)
@bot.message_handler(commands=['start'])
def start(message):
      bot.send_message(message.chat.id, msg1)
bot.polling(none_stop=True)
