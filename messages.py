msg1 = '🤖 Я - нейросеть, которая ищет приватные фото в тысячах баз по всему интернету.\n' \
      '🔐 Могу найти даже самые скрытые фото, о которых остальные даже и не слышали!\n'\
      '_\n'\
      '🔎 Отправьте боту ссылку на страничку ВКонтакте, Instagram, Telegram или номер телефона!\n'\
      'Поддержка: intim_bot@protonmail.com\n'\
      '____\n'\
      'Пользуясь ботом вы соглашаетесь с офертой на оказание информационных услуг.'

msg2 = '🔥 Выбери, где будем искать'

msg3 = '🔗 Отправьте боту ссылку на страницу, или ID пользователя ВК\n'\
       'Пример:\n'\
       '├ https://vk.com/buzova_olga\n'\
       '└ vk.com/buzova_olga'

msg4 = '🔗 Отправьте боту ссылку на страницу Instagram\n'\
       'Пример:\n'\
       '├ http://www.instagram.com/buzova86\n'\
       '├ https://instagram.com/buzova86\n'\
       '├ www.instagram.com/buzova86\n'\
       '├ instagram.com/buzova86\n'\
       '└ https://instagram.com/buzova86?utm_medium=copy_link'

msg5 = '🔗 Отправьте боту ссылку на профиль Телеграм\n'\
       'Пример:\n'\
       '├ @Le_li_ck\n'\
       '└ https://t.me/Le_li_ck'


msg6 = '🔗 Отправьте боту номер телефона. Поиск происходит по базам Telegram и WhatsApp\n'\
       'Пример:\n'\
       '├ +79111234567\n'\
       '├ +380444618061\n'\
       '└ +375291234567'

msg7 = 'Для продолжения решите задачу: 6 + 4'
msg8 = 'Вы прошли проверку!'
msg9 = 'Идёт поиск... 🔎'
msg10 = '✅ Страница найдена в базе\n'\
        '⏳Отправка материала...\n'\

msg11 = 'Профиль не найден'

import random
import datetime

date = str(random.randint(10, 30))+'.0'+str(random.randint(8,9))+'.2022'
def msg12(login):
    return  'Слив найден ✅\n'\
            f'Имя пользователя: {login}\n'\
            f'ID:{random.randint(12312422,74345639)}\n'\
            f'Дата слива:{date}\n'\
            f'Интим фото:{random.randint(20, 40)} шт. ✅\n'\
            f'Интим видео:{random.randint(2, 14)} шт. ✅\n'