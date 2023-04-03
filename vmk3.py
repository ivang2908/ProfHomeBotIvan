import telebot

bot = telebot.TeleBot(token = "6000765846:AAH9Nm9JfhgOQm7fBP63ILco4uzdcr1cxCo")

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
    "\n /place - показывает место в очереди; \n"
    "\n/remove_que - отменить свою очередь, если она была назначена на кп; \n"
    "\n /stop - остановка участия команды, при котором они больше не проходят кп; \n"
    "\n /list_free - команда показывает свободные кпшки\n")

@bot.message_handler(commands = ["reg","yes"])
def reg(message):
    message1 = bot.send_message(message.chat.id, "Введите фамилию")
    bot.register_next_step_handler(message1, name)
    message_to_save1 = message.text


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
    message5 = bot.send_message(message.chat.id, "\n Добавить участника\n"
                                "\n /yes - команда ""добавить участника""\n"
                                "\n /no - всю команду записали!")
    #не понимаю, как сделать, чтобы после ввода команды можно было начать заново добавлять пользователей
    bot.register_next_step_handler(message5, kon)
    message_to_save5 = message.text
    print(message_to_save5)

def kon(message):
    message_to_save6 = message.text
    print(message_to_save6)


@bot.message_handler(commands=["balance"])
def balance(message):
    bot.send_message(message.chat.id, '<b>Ваш баланс:</b>',parse_mode='HTML')
    bot.send_message(message.chat.id, "Вывести баланс из БД")

@bot.message_handler(commands=["transfare"])
def transfer(message):
    message1 = bot.send_message(message.chat.id, "Сколько хотите перевести?")
    bot.register_next_step_handler(message1, id_team)
    n = message.text
    print(n)
def id_team(message):
    message2 = bot.send_message(message.chat.id, "Кому хотите перевести? (id команды)")
    bot.register_next_step_handler(message2, end_t)
    m = message.text
    print(m)
def end_t(message):
    bot.send_message(message.chat.id, "Перевод выполнен!")
    m = message.text
    print(m)

@bot.message_handler(commands=["que_to"])
def que(message):
    message1 = bot.send_message(message.chat.id, "Введите номер КП")
    bot.register_next_step_handler(message1, end_que)
    number = message.text
    print(number)
def end_que(message):
    bot.send_message(message.chat.id, "Вы забронировали место!")

@bot.message_handler(commands=["place"])
def plc(message):
    bot.send_message(message.chat.id, "<b>Ваше место в очереди:</b>", parse_mode='HTML')
    bot.send_message(message.chat.id, "Место в очереди из БД")

@bot.message_handler(commands=["remove_que"])
def rem_q(message):
    bot.send_message(message.chat.id, "Регистрация отменена")

@bot.message_handler(commands=["end"]) #почему-то /stop не работает
def end(message):
    bot.send_message(message.chat.id, "<b> Игра окончена</b>", parse_mode='HTML')
    bot.send_message(message.chat.id, "Спасибо за участие")

@bot.message_handler(commands=["list_free"])
def list(message):
    bot.send_message(message.chat.id, "<b>Сейчас свободна(ы):</b>", parse_mode='HTML')
    bot.send_message(message.chat.id, "Вывести свободные КП")


@bot.message_handler(commands = ["start_kps"])

def start_kp(message):
    bot.send_message(message.chat.id, "Здравствуй, добрый человек!")
    bot.send_message(message.chat.id, "Да прибудет с тобой сила!")
    #интсрукция для КПШников
    bot.send_message(message.chat.id, "<b>Команды бота:</b>\n", parse_mode='HTML')
    bot.send_message(message.chat.id, "\n /start_kps - запуск бота и инструкций; \n"
    "\n /reg_kp - запуск регистрации для участников; \n"
    "\n /balance - показывает, сколько команда заработала вмкешей на данный момент; \n"
    "\n /transfare <n> to <m> - перевести n вмкешей команде с id m; \n"
    "\n /que_to <l> - занять очередь на кп l; \n"
    "\n /place - показывает место в очереди; \n"
    "\n/remove_que - отменить свою очередь, если она была назначена на кп; \n"
    "\n /stop - остановка участия команды, при котором они больше не проходят кп; \n"
    "\n /list_free - команда показывает свободные кпшки\n")

@bot.message_handler(commands=["reg_kp"])
def reg_kp(message):
    message1 = bot.send_message(message.chat.id, "Введите номер КП")
    bot.register_next_step_handler(message1, end_reg)
    d = message.text
    print(d)
def end_reg(message):
    bot.send_message(message.chat.id, "КП успешно зарегистрирована")
    m = message.text
    print(m)

@bot.message_handler(commands=["reg_team"])
def reg_tm(message):
    bot.send_message(message.chat.id, "Команда успешно зарегистрирована")
    bot.send_message(message.chat.id, "Ваш номер:")

@bot.message_handler(commands=["que_team"])
def que_tm_id(message):
    message1 = bot.send_message(message.chat.id, "Введите id команды")
    bot.register_next_step_handler(message1, que_tm_num)
    message_to_save1 = message.text
    print(message_to_save1)

def que_tm_num(message):
    message2 = bot.send_message(message.chat.id, "Введите номер КП")
    bot.register_next_step_handler(message2, que_tm_end)
    message_to_save2 = message.text
    print(message_to_save2)

def que_tm_end(message):
    bot.send_message(message.chat.id, "Команда успешно поставлена в очередь")
    message_to_save3 = message.text
    print(message_to_save3)

@bot.message_handler(commands=["remove_team_que"])
def rem_que_tm_id(message):
    message1 = bot.send_message(message.chat.id, "Введите id команды")
    bot.register_next_step_handler(message1, rem_que_tm_id_2)
    message_to_save1 = message.text
    print(message_to_save1)
def rem_que_tm_id_2(message):
    bot.send_message(message.chat.id, "Команда успешно удалена из очереди")
    message_to_save2 = message.text
    print(message_to_save2)

@bot.message_handler(commands=["transfare_team_money"])

def ttm(message):
    message1 = bot.send_message(message.chat.id, "Введите ID команды 1")
    bot.register_next_step_handler(message1, ttm_2)
    message_to_save1 = message.text
    print(message_to_save1)

def ttm_2(message):
    message2 = bot.send_message(message.chat.id, "Введите ID команды 2")
    bot.register_next_step_handler(message2, ttm_3)
    message_to_save2 = message.txt
    print(message_to_save2)

def ttm_3(message):
    bot.send_message(message.chat.id, "Перевод успешно выполнен")
    message_to_save3 = message.text
    print(message_to_save3)

@bot.message_handler(commands=["payment"])

def payment(message):
    message1 = bot.send_message(message.chat.id, "Введите сумму:")
    bot.register_next_step_handler(message1, payment_2)
    message_to_save1 = message.txt
    print(message_to_save1)
def payment_2(message):
    bot.send_message(message.chat.id, "Оплата произведена")
    message_to_save2 = message.txt
    print(message_to_save2)

@bot.message_handler(commands=["payment_nal"])
def pay_nal(message):
    message1 = bot.send_message(message.chat.id, "Введите сумму:")
    bot.register_next_step_handler(message1, pay_nal_2)
    message_to_save1 = message.txt
    print(message_to_save1)

def pay_nal_2(message):
    bot.send_message(message.chat.id, "Оплата произведена")
    message_to_save2 = message.txt
    print(message_to_save2)

@bot.message_handler(commands=["reg_kp"])
def reg(message):
    message1 = bot.send_message(message.chat.id, 'Введите номер кп')
    bot.register_next_step_handler(message1, reg_2)
    message_to_save = message.txt
    print(message_to_save)
def reg_2(message):
    bot.send_message(message.chat.id, 'КП зарегистрирована')


    
################################################################################################################################
#Вот отсюда перестал работать. Не пойму почему. Писал те же самые команды. Бот обрабатывает команды, но не отвечает:(

@bot.message_handler(commands=['start_team'])
def start_tm(message):
    bot.send_message(message.chat.id, 'Команда вызвана') #посмотреть

@bot.message_handler(commands=['stop_team'])
def stop_tm(message):
    bot.send_message(message.chat.id, 'Команда завершила прохождение КП') #посмотреть

@bot.message_handler(commands=["pay"])
def pay(message):
    message1 = bot.send_message(message.chat.id, "Введите сумму")
    bot.register_next_step_handler(message1, pay_2)
    message_to_save1 = message.txt
    print(message_to_save1)
def pay_2(message):
    bot.send_message(message.chat.id,"Оплата произвдена")#посмотреть почему-то команды перестали работать

@bot.message_handler(commands=["pay_nal"])
def pay_n(message):
    message1 = bot.send_message(message.chat.id, "Введите сумму")
    bot.register_next_step_handler(message1, pay_2)
    message_to_save1 = message.txt
    print(message_to_save1)

def pay_n_2(message):
    bot.send_message(message.chat.id,"Оплата произвдена")#посмотреть почему-то команды перестали работать

@bot.message_handler(commands=["kp_que_team"])
def kp_que(message):
    message1 = bot.send_message(message.chat.id, "Введите ID команды")
    bot.register_next_step_handler(message1, kp_que_2)
    message_to_save1 = message.txt
    print(message_to_save1)
def kp_que_2(message):
    bot.send_message(message.chat.id, "Команда поставлена в очередь")

@bot.message_handler(commands=["kp_balance"])
def kp_bal(message):
    message1 = bot.send_message(message.chat.id, "Введите ID КП")
    bot.register_next_step_handler(message1, kp_bal_2)
    message_to_save1 = message.txt
    print(message_to_save1)
def kp_bal_2(message):
    message2 = bot.send_message(message.chat.id, "Баланс КП:")
    bot.register_next_step_handler(message2, kp_bal_3)
    message_to_save1 = message.txt
    print(message_to_save1)

def kp_bal_3(message):
    bot.send_message(message.chat.id, "Вывести баланс")


bot.polling()