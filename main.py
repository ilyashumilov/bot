import os
import time
import telebot
from telebot.types import InputMediaPhoto

from markups import *
from messages import *
from parsers import *
from editor import *

token = os.getenv('TOKEN')
token1 = os.getenv('TOKEN1')

bot = telebot.TeleBot(token)
bot1 = telebot.TeleBot(token1)

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
            bot.send_message(message.chat.id, msg9)
            try:
                  parsers().ig_parser(login)

                  bot.send_message(message.chat.id, msg10)
                  time.sleep(3)

                  im_editor(login)

                  media_group = []
                  for num in [1,2]:
                        media_group.append(InputMediaPhoto(open(f'img/out{num}.png', 'rb'),
                                                           caption=msg12(login) if num == 1 else ''))
                  bot.send_media_group(chat_id=message.chat.id, media=media_group)
                  time.sleep(2)
                  bot.send_message(message.chat.id, msg13(login), reply_markup=markup3)

            except Exception as e:
                  print(e)
                  bot.send_message(message.chat.id, msg11)

      elif 't.me' in message.text or '@' in message.text:
            if 't.me' in message.text:
                  list = [pos for pos, char in enumerate(message.text) if char == '/']
                  login = message.text[list[-1] + 1:]
            else:
                  login = message.text
            bot.send_message(message.chat.id, msg9)

            try:
                  parsers().tg_parser(login)

                  bot.send_message(message.chat.id, msg10)
                  time.sleep(3)

                  im_editor(login)

                  media_group = []
                  for num in [1,2]:
                        media_group.append(InputMediaPhoto(open(f'img/out{num}.png', 'rb'),
                                                           caption=msg12(login) if num == 1 else ''))
                  bot.send_media_group(chat_id=message.chat.id, media=media_group)
                  time.sleep(2)
                  bot.send_message(message.chat.id, msg13(login), reply_markup=markup3)

            except Exception as e:
                  print(e)
                  bot.send_message(message.chat.id, msg11)

      elif 'vk' in message.text:
            list = [pos for pos, char in enumerate(message.text) if char == '/']
            login = message.text[list[-1] + 1:]
            bot.send_message(message.chat.id, msg9)
            try:
                  parsers().vk_parser(login)
                  bot.send_message(message.chat.id, msg10)
                  time.sleep(1)
                  im_editor(login)

                  media_group = []
                  for num in [1,2]:
                        media_group.append(InputMediaPhoto(open(f'img/out{num}.png', 'rb'),
                                                           caption=msg12(login) if num == 1 else ''))
                  bot.send_media_group(chat_id=message.chat.id, media=media_group)
                  time.sleep(2)
                  bot.send_message(message.chat.id, msg13(login), reply_markup=markup3)


            except Exception as e:
                  print(e)
                  bot.send_message(message.chat.id, msg11)

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
