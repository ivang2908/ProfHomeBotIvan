import telebot
bot = telebot.TeleBot(token = "6000765846:AAFp7pHHTWkQCdqZwrurQi5JYdswVyDla04")
@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет!")
    #интсрукция
    bot.send_message(message.chat.id, "<b>Команды бота:</b>\n", parse_mode='HTML')
    bot.send_message(message.chat.id, "\n /start - запуск бота и инструкций; \n"
    "\n /reg - запуск регистрации для участников; \n"
    "\n /balance - показывает, сколько команда заработала вмкешей на данный момент; \n"
    "\n /transfare <n> to <m> - перевести n вмкешей команде с id m; \n"
    "\n /que_to <l> - занять очередь на кп l; \n"
    "\n/remove_que - отменить свою очередь, если она была назначена на кп; \n"
    "\n /stop - остановка участия команды, при котором они больше не проходят кп; \n"
    "\n /list_free - команда показывает свободные кпшки\n")

@bot.message_handler(commands = ["reg","yes"])
def reg(message):
    message1 = bot.send_message(message.chat.id, "Введите фамилию")
    bot.register_next_step_handler(message1, name)
    message_to_save1 = message.text
    print(message_to_save1)
def name(message):
    message2 = bot.send_message(message.chat.id, "Введите имя")
    bot.register_next_step_handler(message2, otch)
    message_to_save2 = message.text
    print(message_to_save2)
def otch(message):
    message3 = bot.send_message(message.chat.id, "Введите отчество")
    bot.register_next_step_handler(message3, group)
    message_to_save3 = message.text
    print(message_to_save3)
def group(message):
    message4 = bot.send_message(message.chat.id, "Введите номер группы")
    bot.register_next_step_handler(message4, last)
    message_to_save4 = message.text
    print(message_to_save4)
def last(message):
    message4 = bot.send_message(message.chat.id, "\n Добавить участника\n"
                                "\n /да - команда ""добавить участника""\n"
                                "\n /нет - всю команду записали!")
    #не понимаю, как сделать, чтобы после ввода команды можно было начать заново добавлять пользователей
    bot.register_next_step_handler(message4, end)
    message_to_save5 = message.text
    print(message_to_save5)
def end(message):
    message_to_save6 = message.text
    print(message_to_save6)


@bot.message_handler(commands = ["balance"])
def balance(message):
    bot.send_message(message.chat.id, '\n <b>Ваш баланс</b<\n',parse_mode='HTML'
                     "Вывести баланс из БД")


bot.polling()