import os
import time
import telebot
from markups import *
from messages import *
from parsers import *

token  =  os.getenv('TOKEN')
token1  =  os.getenv('TOKEN1')

bot=telebot.TeleBot(token)
bot1=telebot.TeleBot(token1)

@bot.message_handler(content_types=['text'])
def handler(message):
      if message.text == '/start':
            bot.send_message(message.chat.id, msg1, reply_markup=markup1)

      elif message.text == '🔎 Поиск':
            bot.send_message(message.chat.id, msg2, reply_markup=markup2)

      elif message.text == '10':
            # bot.send_message(message.chat.id, msg8)
            # time.sleep(2)
            bot.send_message(message.chat.id, msg9)
            bot1.send_message(message.chat.id, 'bot1')

      elif message.text.isnumeric():
            bot.send_message(message.chat.id, msg7)

      elif 'instagram' in message.text:
            list = [pos for pos, char in enumerate(message.text) if char == '/']
            login = message.text[list[-1] + 1:]
            print(login)
            parsers.ig_parser(login)


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
