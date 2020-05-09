import telebot

bot = telebot.TeleBot('1172539884:AAFPxRvLtXc9jqryRUmq3x5pB5TJHVywyrI')

from telebot import types

# Метод, который получает сообщения и обрабатывает их
sp_hello = ['привет', 'hi', 'здравствуйте', 'ку', 'hello','здаров','превед']
answers = ['да', 'нет']
national = ['норвежец','англичанин','украинец','испанец']
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global flag
    if message.text.lower() in sp_hello:
        bot.send_message(message.from_user.id,
                         "Привет, многие великие люди придумывали непростые задачи на логику. Выбирай из списка человека, от которого хочешь задачу.")

        keyboard = types.InlineKeyboardMarkup()

        key_einsh = types.InlineKeyboardButton(text='Задача от Альберта Эйнштейна', callback_data='einsh')
        keyboard.add(key_einsh)

        bot.send_message(message.from_user.id, text='Выбери человека, от которого хочешь задачу.', reply_markup=keyboard)

    elif message.text.lower() == 'да':
        if flag == 1:
            keyboard = types.InlineKeyboardMarkup()
            key_einsh = types.InlineKeyboardButton(text='Норвежец', callback_data='einsh_1_1')
            keyboard.add(key_einsh)
            key_telec = types.InlineKeyboardButton(text='Англичанини', callback_data='einsh_1_2')
            keyboard.add(key_telec)
            key_bliznecy = types.InlineKeyboardButton(text='Украинец', callback_data='einsh_1_2')
            keyboard.add(key_bliznecy)
            key_bliznecy = types.InlineKeyboardButton(text='Японец', callback_data='einsh_1_2')
            keyboard.add(key_bliznecy)
            key_bliznecy = types.InlineKeyboardButton(text='Испанец', callback_data='einsh_1_2')
            keyboard.add(key_bliznecy)

            bot.send_message(message.from_user.id, text='Давай попробуем, кто же пьёт воду ?', reply_markup=keyboard)
    elif message.text.lower() == 'нет':
        bot.send_message(message.from_user.id,'Жаль, ну ничего. Решим в следующий раз!')

    elif message.text.lower() in national:
        bot.send_message(message.from_user.id, 'Хорошенько подумай.')
    elif message.text.lower() == 'японец':
        bot.send_message(message.from_user.id, 'Так держать, молодец! Вам с Эйнштейном было бы о чём поговорить. \nЧтобы начать заново, напиши "Привет".')
    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши 'Привет'")
    elif message.text == "/start":

        bot.send_message(message.from_user.id, "Следует начинать с приветствия :)\n")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

flag = 0
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global flag
    if call.data == "einsh":
        vved = 'Конечно, во времена Эйнштейна крипты не было, но вместо этого могла быть валюта. Суть и сложность задачи от этого не меняется.'
        msg = 'Эйнштейн предлагал решить подобную задачу, не используя посторонних пердметов(т.е "в голове", без тетрадей и ручек)\n1. На улице стоят пять домов\n2. Англичанин живёт в красном доме. \n3. У испанца есть собака. \n4. В зелёном доме пьют кофе. \n5. Украинец пьёт чай. \n6. Зелёный дом стоит сразу справа от белого дома. \n7. Тот, кто майнит Bitcoin, разводит улиток. \n8. В жёлтом доме майнят Ethereum. \n9. В центральном доме пьют молоко. \n10. Норвежец живёт в первом доме. \n11. Сосед того, кто майнит Stellar, держит лису. \n12. В доме по соседству с тем, в котором держат лошадь, майнят Ethereum. \n13. Тот, кто майнит IOTA, пьёт апельсиновый сок. \n14. Японец майнит Monero. \n15. Норвежец живёт рядом с синим домом.\n В целях ясности следует добавить, что каждый из пяти домов окрашен в свой цвет, а их жители — разных национальностей, владеют разными животными, пьют разные напитки и майнят разные криптовалюты. Ещё одно замечание: в утверждении 6 «справа» означает справа относительно вас.'
        quest = 'Вопрос: кто пьёт воду, а кто держит зебру? \n**Чтобы не было спорных моментов, добавим следующее:\n-дома расположены в ряд, друг за другом;\n-один из жильцов точно пьёт воду, и кто-то из жильцов точно держит зебру.'
        sol = 'Решаем ? Напиши Да/Нет'
        flag = 1
        bot.send_message(call.message.chat.id, vved)
        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, quest)
        bot.send_message(call.message.chat.id, sol)
    elif call.data == "einsh_1_1":
        msg = 'Молодец! Кто же держит зебру ? Просто напиши его национальность.'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "einsh_1_2":
        msg = 'Хорошенько подумай.'
        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)