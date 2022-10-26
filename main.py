import telebot
token  =  ('5630810297:AAFNnrm6K198kwqMsLMzd60PbiliRufE6aU')

bot=telebot.TeleBot (token)
@bot.message_handler(commands=['start'])
def start(message):
      bot.send_message(message.chat.id, 'a', parse_mode='html')
bot.polling(none_stop=True)
