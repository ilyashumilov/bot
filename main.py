import requests as r
import telebot
import time

coins = ['IOTA','LUNC','SUSHI']

token = '5766858406:AAGswKF8IfZapYhr3894fj-mi9ospJteprU'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjM1YTZlNTVmYzVhOGFkZmVjNjI0OTExIiwiaWF0IjoxNjY2ODcwODY5LCJleHAiOjMzMTcxMzM0ODY5fQ.lrl5ZJrL046hA5dOmwjy3FrLInXoX3ce6FP6N33Sup4'
bot=telebot.TeleBot(token)

while True:
    for coin in coins:
        resp = r.get(f'https://api.taapi.io/stochrsi?secret={key}&exchange=binance&symbol={coin}/USDT&interval=15m')
        resp1 = r.get(f'https://api.taapi.io/rsi?secret={key}&exchange=binance&symbol={coin}/USDT&interval=15m')
        msg = f'Pair: {coin}USDT int 15m\n' \
              f'StochRSI FastK Value: {"{0:.5g}".format(resp.json()["valueFastK"])}\n' \
              f'StochRSI < 20 -> oversold -> possible long\n' \
              f'StochRSI > 70 -> overbought -> possible short\n'
        print(msg)
        bot.send_message('-1001814658941',msg)
        time.sleep(60)





# import os
# import time
# import telebot
# from markups import *
# from messages import *

# token  =  os.getenv('TOKEN')
# token1  =  os.getenv('TOKEN1')

# bot=telebot.TeleBot(token)
# bot1=telebot.TeleBot(token1)

# @bot.channel_post_handler(func=lambda m: True,content_types=['text'])
# def handler(message):
#       if message.text == '/start':
#             bot.send_message(message.chat.id, msg1, reply_markup=markup1)

#       elif message.text == '🔎 Поиск':
#             bot.send_message(message.chat.id, msg2, reply_markup=markup2)

#       elif message.text == '10':
#             # bot.send_message(message.chat.id, msg8)
#             # time.sleep(2)
#             bot.send_message(message.chat.id, msg9)
#             bot1.send_message(message.chat.id, 'bot1')

#       else:
#             bot.send_message(message.chat.id, msg7)

# @bot.callback_query_handler(lambda query: query.data in ["vk"])
# def process_callback_2(query):
#       bot.send_message(query.message.chat.id, msg3)

# @bot.callback_query_handler(lambda query: query.data in ["ig"])
# def process_callback_2(query):
#       bot.send_message(query.message.chat.id, msg4)

# @bot.callback_query_handler(lambda query: query.data in ["tg"])
# def process_callback_2(query):
#       bot.send_message(query.message.chat.id, msg5)

# @bot.callback_query_handler(lambda query: query.data in ["no"])
# def process_callback_2(query):
#       bot.send_message(query.message.chat.id, msg6)

# bot.polling(none_stop=True)
