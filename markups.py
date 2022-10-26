from telebot import types

markup1 = types.ReplyKeyboardMarkup()
item1 = types.KeyboardButton("🔎 Поиск")
markup1.add(item1)