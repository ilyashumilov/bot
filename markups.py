from telebot import types

markup1 = types.ReplyKeyboardMarkup()
item1 = types.KeyboardButton("🔎 Поиск")
markup1.add(item1)


markup2 = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton("🌐 ВКонтакте")
item2 = types.InlineKeyboardButton("📷 Instagram")
item3 = types.InlineKeyboardButton("👤 Телеграм")
item4 = types.InlineKeyboardButton("📞 Номер телефона")
markup2.add(item1,item2,item3,item4)

