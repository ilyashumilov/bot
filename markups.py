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

# markup3 = types.InlineKeyboardMarkup()
# item1 = types.InlineKeyboardButton("Приобрести 💳 | 399 ₽", callback_data='limit_pay')
# item2 = types.InlineKeyboardButton("Купить безлимит ♾️ | 990 ₽", callback_data='unlimit_pay')
#
# markup3.row(item1)
# markup3.row(item2)


def markup3(key):
    url = f'https://oplata.qiwi.com/create?publicKey={key}&readonly_extras=cf1&amount='
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton.WithUrl(text="Приобрести 💳 | 399 ₽", url=url+'399.00')
    item2 = types.InlineKeyboardButton.WithUrl(text="Купить безлимит ♾️ | 990 ₽",url=url+'990.00')
    markup.row(item1)
    markup.row(item2)
    return markup



