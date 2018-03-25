# -*- coding: utf-8 -*-
TOKEN = '433340494:AAG_h5rM2oB_l3QOiNH_jlgskgd-QXePGD4'

import time
import telepot
from dbhelper1 import DBHelper
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
from quote import writer, quote

def congrats(sender):
    bot = telepot.Bot(TOKEN)
    conn = DBHelper._ini_()
    keyboard = ReplyKeyboardMarkup(keyboard=[['Share my Thought'], ['Listen to a Thought']], one_time_keyboard=True, resize_keyboard=True)
    congrats = """Congratulations! \nYour thought has received the top 10 numbers of “like” for the past period. Please check the list! Hope that more popular thoughts can be shared from you! \nThank you for talking to Agony!"""
    bot.sendMessage(sender,congrats,reply_markup = keyboard)
    conn.close()
