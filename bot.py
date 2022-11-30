import telebot

bot = telebot.TeleBot(token = "5934474666:AAFnakAtj1d6g8kwDk6SBLWO4tB8tnPogYs")

@bot.message_handler(func = lambda msg: msg.text in ["Привет", "Здарова","Утро доброе","Здаров","Hello","Hi","привет"])
def Hello_handler(message: telebot.types.Message):
    bot.send_message(chat_id = message.chat.id, text = "Здарова!")

@bot.message_handler(func = lambda msg: msg.text in ["Понедельник","понедельник"])
def Monday_handler(message: telebot.types.Message):
    bot.send_message(chat_id = message.chat.id, text = "Понедельник - День Бездельник \n"
                                                           "\n1 Пара - БЖД (614)\n"
                                                           "\n2 Пара - Алгебра и Геометрия (П-5)\n"
                                                           "\n3 Пара - Алгебра и Геометрия (605)\n"
                                                           "\n4 Пара - Физическая культура\n"
                                                           "\n5 Пара - Алгоритмы и алгоритмические языки (П-6)")


@bot.message_handler(func = lambda msg: msg.text in ["Вторник","вторник"])
def Tuesday_handler(message: telebot.types.Message):
    bot.send_message(chat_id = message.chat.id, text = "Вторник - Повторник\n"
                                                           "\n1 Пара - Математический анализ (П-5)\n"
                                                           "\n2 Пара - Практикум на ЭВМ (72)\n"
                                                           "\n3 Пара - Математический анализ (549)")

@bot.message_handler(func = lambda msg: msg.text in ["Среда","среда"])
def Wednesday_handler(message: telebot.types.Message):
    bot.send_message(chat_id = message.chat.id, text = "Среда - Тамада\n"
                                                           "\n2 Пара - Алгебра и Геометрия (П-5)\n"
                                                           "\n3 Пара - Математический анализ (П-5)")

@bot.message_handler(func = lambda msg: msg.text in ["Четверг","четверг"])
def Thursday_handler(message: telebot.types.Message):
    bot.send_message(chat_id = message.chat.id, text = "Четверг - все заботы я отверг \n"
                                                           "\n1 Пара - Математический анализ (503)\n"
                                                           "\n2 Пара - История (505)\n"
                                                           "\n3 Пара - Алгебра и Геометрия (645)\n"
                                                           "\n4 Пара - Практикум на ЭВМ (72)\n"
                                                           "\n 5 Пара - История (П5)")

@bot.message_handler(func = lambda msg: msg.text in ["Пятница","пятница"])
def Friday_handler(message: telebot.types.Message):
    bot.send_message(chat_id = message.chat.id, text = " Пятница - пьяница\n"
                                                           "\n1 Пара - Физическая культура\n"
                                                           "\n2 Пара - Алгоритмы и алгоритмические языки (П-5)\n"
                                                           "\n3 Пара - Английский язык (778,740)\n"
                                                           "\n4 Пара - Английский язык (778,740)")
@bot.message_handler(func = lambda msg: msg.text in ["Cуббота","суббота"])
def Saturday_handler(message: telebot.types.Message):
    bot.send_message(chat_id = message.chat.id, text = "Суббота - не работа\n"
                                                           "\nИди отдыхай!!!")

@bot.message_handler(func = lambda msg: msg.text in ["Воскресенье","воскресенье"])
def Sunday_handler(message: telebot.types.Message):
    bot.send_message(chat_id = message.chat.id, text = "Воскресенье - день веселья\n"
                                                           "\nОТДЫХАЙ ПО ПОЛНОЙ!!!\n"
                                                           "Но не забывай: завтра в Универ")

@bot.message_handler(content_types = telebot.util.content_type_media)
def text_message_handler(message: telebot.types.Message):
    if message.text:
        bot.send_message(chat_id = message.chat.id, text = 'Что желаете, Коллега)?')
    elif message.photo:
        bot.send_message(chat_id = message.chat.id, text = "Лучше, чем лекции на ВМК!")
    elif message.sticker:
        bot.send_message(chat_id = message.chat.id, text = "ХЕ ХЕ :)")
    elif message.animation:
        bot.send_message(chat_id=message.chat.id, text="Отправь старосте для коллекции!!!")
if __name__ == "__main__":
    bot.infinity_polling()

