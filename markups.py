from telebot import types

markup1 = types.ReplyKeyboardMarkup()
item1 = types.KeyboardButton('🔎 Поиск')
markup1.add(item1)


markup2 = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton("🌐 ВКонтакте", callback_data='vk')
item2 = types.InlineKeyboardButton("📷 Instagram", callback_data='ig')
item3 = types.InlineKeyboardButton("👤 Телеграм", callback_data='tg')
item4 = types.InlineKeyboardButton("📞 Номер телефона", callback_data='no')
markup2.row(item1)
markup2.row(item2)
markup2.row(item3)
markup2.row(item4)


