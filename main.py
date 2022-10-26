import os
import telebot
token  =  os.getenv('TOKEN')

print(token)

bot=telebot.TeleBot (token)
@bot.message_handler(commands=['start'])
def start(message):
      bot.send_message(message.chat.id, 'a', parse_mode='html')
bot.polling(none_stop=True)
