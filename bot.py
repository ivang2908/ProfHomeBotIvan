import telebot

bot = telebot.TeleBot(token = "5934474666:AAE2Oq8uHjcyDDqD3Oj7CwabB_FHyO6Vq_Y")

@bot.message_handler(commands = ["Привет", "Здарова","Утро доброе","Здаров","Hello","Hi"])
def Привет_handler(message: telebot.types.Message):
    if message.text:
        bot.send_message(chat_id = message.chat.id, text = "Здарова!")

@bot.message_handler(commands = ["Понедельник","понедельник"])
def Понедельник_handler(message: telebot.types.Message):
    if message.text:
        bot.send_message(chat_id = message.chat.id, text = "Понедельник - День Бездельник \n"
                                                           "\n1 Пара - БЖД (614)\n"
                                                           "\n2 Пара - Алгебра и Геометрия (П-5)\n"
                                                           "\n3 Пара - Алгебра и Геометрия (605)\n"
                                                           "\n4 Пара - Физическая культура\n"
                                                           "\n5 Пара - Алгоритмы и алгоритмические языки (П-6)")


@bot.message_handler(commands = ["Вторник","вторник"])
def Вторник_handler(message: telebot.types.Message):
    if message.text:
        bot.send_message(chat_id = message.chat.id, text = "Вторник - Повторник\n"
                                                           "\n1 Пара - Математический анализ (П-5)\n"
                                                           "\n2 Пара - Практикум на ЭВМ (72)\n"
                                                           "\n3 Пара - Математический анализ (549)")

@bot.message_handler(commands = ["Среда","среда"])
def Среда_handler(message: telebot.types.Message):
    if message.text:
        bot.send_message(chat_id = message.chat.id, text = "Среда - Тамада\n"
                                                           "\n2 Пара - Алгебра и Геометрия (П-5)\n"
                                                           "\n3 Пара - Математический анализ (П-5)")

@bot.message_handler(commands = ["Четверг","четверг"])
def Четверг_handler(message: telebot.types.Message):
    if message.text:
        bot.send_message(chat_id = message.chat.id, text = "Четверг - все заботы я отверг \n"
                                                           "\n1 Пара - Математический анализ (503)\n"
                                                           "\n2 Пара - История (505)\n"
                                                           "\n3 Пара - Алгебра и Геометрия (645)\n"
                                                           "\n4 Пара - Практикум на ЭВМ (72)\n"
                                                           "\n 5 Пара - История (П5)")

@bot.message_handler(commands = ["Пятница","пятница"])
def Пятница_handler(message: telebot.types.Message):
    if message.text:
        bot.send_message(chat_id = message.chat.id, text = " Пятница - пьяница\n"
                                                           "\n1 Пара - Физическая культура\n"
                                                           "\n2 Пара - Алгоритмы и алгоритмические языки (П-5)\n"
                                                           "\n3 Пара - Английский язык (778,740)\n"
                                                           "\n4 Пара - Английский язык (778,740)")
@bot.message_handler(commands = ["Cуббота","суббота"])
def Суббота_handler(message: telebot.types.Message):
    if message.text:
        bot.send_message(chat_id = message.chat.id, text = "Суббота - не работа\n"
                                                           "\nИди отдыхай!!!")

@bot.message_handler(commands = ["Воскресенье","воскресенье"])
def Воскресенье_handler(message: telebot.types.Message):
    if message.text:
        bot.send_message(chat_id = message.chat.id, text = "Воскресенье - день веселья\n"
                                                           "\nОТДЫХАЙ ПО ПОЛНОЙ!!!\n"
                                                           "Но не забывай: завтра в Универ")

@bot.message_handler(content_types = ["text", "photo","sticker"])
def text_message_handler(message: telebot.types.Message):
    if message.text:
        bot.send_message(chat_id = message.chat.id, text = 'Что желаете, Коллега)?')
    elif message.photo:
        bot.send_message(chat_id = message.chat.id, text = "Лучше, чем лекции на ВМК!")
    elif message.sticker:
        bot.send_message(chat_id = message.chat.id, text = "ХЕ ХЕ :)")
    elif message.sticker:
        bot.send_message(chat_id = message.chat.id, text = "ХЕ ХЕ :)")
if __name__ == "__main__":
    bot.infinity_polling()

