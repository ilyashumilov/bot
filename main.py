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

@bot.callback_query_handler(lambda query: query.data in ["vk"])
def process_callback_2(query):
      bot.send_message(query.message.chat.id, msg3)

@bot.callback_query_handler(lambda query: query.data in ["ig"])
def process_callback_2(query):
      bot.send_message(query.message.chat.id, msg4)

@bot.callback_query_handler(lambda query: query.data in ["tg"])
def process_callback_2(query):
      bot.send_message(query.message.chat.id, msg5)

@bot.callback_query_handler(lambda query: query.data in ["no"])
def process_callback_2(query):
      bot.send_message(query.message.chat.id, msg6)

bot.polling(none_stop=True)
