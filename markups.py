from telebot import types

markup1 = types.ReplyKeyboardMarkup()
item1 = types.KeyboardButton("🔎 Поиск")
markup1.add(item1)


markup2 = types.ReplyKeyboardMarkup()
item1 = types.KeyboardButton("🌐 ВКонтакте")
item2 = types.KeyboardButton("📷 Instagram")
item3 = types.KeyboardButton("👤 Телеграм")
item4 = types.KeyboardButton("📞 Номер телефона")
markup2.add(item1,item2,item3,item4)

