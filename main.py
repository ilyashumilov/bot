import os
import telebot
from markups import *
from messages import *

token  =  os.getenv('TOKEN')
bot=telebot.TeleBot (token)

@bot.message_handler(content_types=['text'])
def handler(message):
      if message.text == '/start':
            bot.send_message(message.chat.id, msg1, reply_markup=markup1)

      if message.text == '🔎 Поиск':
            bot.send_message(message.chat.id, msg2, reply_markup=markup2)


bot.polling(none_stop=True)
