# -*- coding: utf-8 -*-
TOKEN = 'Your own token'

import time
import telepot
from dbhelper1 import DBHelper
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
from quote import writer, quote

def publish(announcement):
    bot = telepot.Bot(TOKEN)
    conn = DBHelper._ini_()
    keyboard = ReplyKeyboardMarkup(keyboard=[['Share my Thought'], ['Listen to a Thought']], one_time_keyboard=True, resize_keyboard=True)
    alluser = DBHelper.get_all_user(conn)
    for user in alluser:
        bot.sendMessage(user[0],announcement,reply_markup = keyboard)
        conn.close()

a= "Hello guys!  How is everything going? I am your Agony Aunt!\nToday is Friday, our weekly ranking announcing day! Here I am proud to tell you the top ten liked thoughts during the past week!"
b= "The gold medal winner:\n'Adrian can decode more than python. Wanna try him? ;)'\n\nThe first runner-up:\n'College is a little overwhelming... anyone feel the same way'\n\nThe third place thought:\n'Like if you like Tori Black'\n\nThen follows the 4-10th most liked thoughts:\n'sia！interesting bot！'\n'Life's tough but what's life without some hiccups'\n'Hi nice to meet you ❤️❤️❤️❤️❤️❤️'\n'ENROLLING IN COMPUTER SCIENCE IS THE BEST DECISION I HAVE EVER MADE!!!❤️❤️❤️'\n'How do I feel less bad about being single? :('\n'Watching wk 5 lectures now..'\n'I'm hungry can I eat someone'"
c= "Thank you guys for sharing amazing thoughts! \nCome on guys, let’s share and reply!  Little little thoughts, big big network!"


publish(c)

