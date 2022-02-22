import telebot
from telebot import types
import config
import time
import sqlite3

bot = telebot.TeleBot(config.token)

hi =['hi', 'hello', 'привет', 'привіт']
nope = ['no', 'nope', 'never', 'нет', 'ні']
ye = ['yes', 'да', 'так', 'согласен']


@bot.message_handler(content_types='text')
def message_text(message):
    """
    user message processing
    :param message: message
    :return: answer
    """

    new_row = (message.from_user.id, message.from_user.first_name,message.from_user.last_name, '', '', '')
    conn = sqlite3.connect('telebot.db')
    cur = conn.cursor()
    sql = "SELECT * FROM user WHERE userid =?"
    cur.execute(sql, [(message.from_user.id)])
    results = cur.fetchone()
    if results == None:
        cur.execute("INSERT INTO user VALUES(?, ?, ?, ?,?,?);", new_row)
        conn.commit()

    cur.execute("SELECT * FROM user")
    results = cur.fetchall()


    if message.text.lower() not in hi and message.text not in nope and message.text not in ye:
        bot.send_message(message.chat.id, f'Добро пожаловать, {message.from_user.first_name}!', '', '')
    elif message.text.lower() in hi:
        return (message_hi(message))
    elif message.text.lower() in ye:
        return (value_yes(message))

    elif message.text.lower() in nope:
        return (value_no(message))


@bot.message_handler(func=lambda x: x.text.lower().startswith('привет'))
def message_hi(message):
    """
    Hi and ask function
    :param message:
    :return:
    """

    bot.send_message(message.chat.id, f'И Вам {what_time()} {message.from_user.first_name} {message.from_user.last_name}'
                                      f'! Хотите узнать больше о нашей продукции? Да/Нет')


@bot.message_handler(func=lambda x: x.text.lower().startswith('да'))
def value_yes(message):
    """
    answer yes function
    :param message:
    :return:
    """
    keyboardV = types.InlineKeyboardMarkup()
    f1= open('1.txt')
    f2 = open('2.txt')
    f3 = open('3.txt')

    kbv1 = types.InlineKeyboardButton(text='qwqwqqwqw', url= 'https://petronek.com/slovko/')
    kbv2 = types.InlineKeyboardButton(text="Продукт2", url= 'https://petronek.com/slovko/')
    kbv3 = types.InlineKeyboardButton(text="Product3", url= 'https://petronek.com/slovko/')
    keyboardV.add(kbv1, kbv2, kbv3)
    bot.send_message(message.chat.id, "Выберите товар: ", reply_markup=keyboardV)


@bot.message_handler(func = lambda x: x.text.lower().startswith('нет'))
def value_no(message):
    bot.send_message(message.chat.id, "Спасибо, что зашли к нам! Хорошего дня! ")


def what_time():
    if int (time.strftime('%H')) < 12:
        return 'доброе утро'
    elif int(time.strftime('%H')) > 17:
        return 'добрый вечер'
    else:
        return 'добрый день'


bot.infinity_polling()
