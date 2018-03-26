# -*- coding: utf-8 -*-
TOKEN = 'Your own token'

import time
import telepot
from dbhelper1 import DBHelper
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
from quote import writer, quote

bot = telepot.Bot(TOKEN)
conn = DBHelper._ini_()
reply_keyboard = ReplyKeyboardMarkup(keyboard=[['I want to reply'],['Share my Thought'],['Listen to a Thought']], one_time_keyboard=True, resize_keyboard=True)
reply_keyboard2 = ReplyKeyboardMarkup(keyboard=[['Like'],['I want to reply',],['Share my Thought',],['Listen to another Thought',],['Report this message as spam',]], one_time_keyboard=True, resize_keyboard=True)
reply_keyboard3 = ReplyKeyboardMarkup(keyboard=[['Like'],['Share my Thought',],['Listen to another Thought',]], one_time_keyboard=True, resize_keyboard=True)
reply_keyboard4 = ReplyKeyboardMarkup(keyboard=[['I want to reply',],['Share my Thought',],['Listen to another Thought',]], one_time_keyboard=True, resize_keyboard=True)
keyboard = ReplyKeyboardMarkup(keyboard=[['Share my Thought'], ['Listen to a Thought']], one_time_keyboard=True, resize_keyboard=True)
keyboard1 = ReplyKeyboardMarkup(keyboard=[['Share another Thought',],[ 'Listen to a Thought',]], one_time_keyboard=True, resize_keyboard=True)
keyboard2 = ReplyKeyboardMarkup(keyboard=[['Confirm', ],[ 'Enter again', ]], one_time_keyboard=True, resize_keyboard=True)
admin_keyboard1 = ReplyKeyboardMarkup(keyboard = [['Post message to all users'], ['Fetch top 10 favorite messages'], ['Send favorite messages to all users']], one_time_keyboard = True, resize_keyboard=True)
confirm_keyboard1 = ReplyKeyboardMarkup(keyboard = [['Confirm Posting'],['Re-enter the message']], one_time_keyboard = True, resize_keyboard = True)
confirm_keyboard2 = ReplyKeyboardMarkup(keyboard = [['Confirm Sending'],['Cancel']], one_time_keyboard = True, resize_keyboard = True)

def conversation(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    update = bot.getUpdates()
    content = msg['text']
    msgid = int(update[0]["update_id"])
    if chat_id == 1:
        if content_type == 'text' and content == '/admin' or content == 'Cancel':       # 在chat——id后面填上我们几个人的ID PS:chatid就是用户的id吧 我忘记了
            bot.sendMessage(chat_id, text='Welcome, you are an admin. Please select from the following functions', reply_markup=admin_keyboard1)
        elif content_type == 'text' and content == ('Post message to all users' or 'Re-enter the message'):
            bot.sendMessage(chat_id, text='Your next message will be sent to all users', reply_markup=confirm_keyboard1)
        elif content_type == 'text' and content == 'Fetch top 10 favorite messages':
#top 10
            bot.sendMessage(chat_id, text='asdfg', reply_markup=admin_keyboard1) # text后面加上获取的top 10 messages
        elif content_type == 'text' and content == 'Send favorite messages to all users':
            bot.sendMessage(chat_id, text='Please confirm sending', reply_markup=confirm_keyboard2)
        elif content_type == 'text' and content == 'Confirm Posting':
            bot.sendMessage(chat_id, text='The message has been sent', reply_markup=admin_keyboard1)
        elif content_type == 'text' and content == 'Confirm Sending':
        # 这一行加上bot给所有人发送top 10 messages
            bot.sendMessage(chat_id, text = 'Top 10 message has been sent to all users', reply_markup=admin_keyboard1)

            # 这一行加上bot给所有人发消息的指令， 消息的内容为post message to all user之后的消息
    else:
        if content_type == 'text' and content == '/start':
            # bot.sendMessage(chat_id, text = 'Hey! There you are. I am agony aunt. I have been hoping to listen to your thoughts, your happiness, your problems and your lives, so as everyone else here. A special topic will be sent to you every day when you open your eyes. Feel free to share and exchange your stories and feelings with us. No personal information will be displayed in this completely anonymous world. Again, welcome!', reply_markup = keyboard)
            bot.sendMessage(chat_id, text = 'Everyone has secrets. Sometimes we hope to tell it, while ending up with finding no one to tell. This time, through agony bot, you can exchange your secret with some strangers in an anonymous way. If you want, you can also reply to the sender, like his or her secret, or just listen. Hey! Please protect these little secrets for their owners, don’t tell anyone else! 24 hours, start exchanging from now!',reply_markup = keyboard)
        elif content_type == 'text' and (content == 'Share my Thought' or content == 'Share another Thought'):
            bot.sendMessage(chat_id, text = 'Hey! Welcome to today’s agony aunt! Please send your message. You will receive a little gift from us once you confirm sending the message :D')
        elif content_type == 'text' and (content == 'Listen to a Thought' or content == 'Listen to another Thought'):
            result = DBHelper.get_message(conn,chat_id)
            DBHelper.add_reply(conn,result[0],"",result[2],result[1],chat_id)
            bot.sendMessage(chat_id,text = result[0],reply_markup=reply_keyboard2)
        elif content_type == 'text' and content == 'I want to reply':
            bot.sendMessage(chat_id, 'Hey! Please enter your comment! It will be posted to the original sender! Hope you two could become friends or just remain strangers :D')
        elif content_type == 'text' and content == 'Like':
            reply = DBHelper.get_reply(conn, chat_id)
            DBHelper.increase_like(conn, reply[2])
            num = DBHelper.get_like(conn, reply[2]) 
            bot.sendMessage(reply[0],"Wow,some one has liked your message:\n"+reply[1])
            bot.sendMessage(reply[0],"This message has been liked " + str(num) +" times.", reply_markup=keyboard)
            bot.sendMessage(chat_id, "You've liked this message",reply_markup = reply_keyboard4)
        elif content_type == 'text' and content == 'Report this message as spam':
            reply = DBHelper.get_reply(conn, chat_id)
            DBHelper.mark_as_spam(conn, reply[2])
            bot.sendMessage(chat_id,"Thanks for your report, our administer will look into this", reply_markup = keyboard1)
        elif content_type == 'text' and content == 'Confirm':
            bot.sendMessage(chat_id,"Receive! Exchanging in progress! Please wait :D\nToday\'s quote for you:\n %s\n %s" % (quote, writer),reply_markup = keyboard1)
        elif content_type == 'text' and content == 'Enter again':
            lastid = DBHelper.last_sent_message(conn, chat_id)
            DBHelper.delete_message(conn,lastid)
            bot.sendMessage(chat_id,"Sure, please enter your message again.")
        else:
            last_message = DBHelper.get_last_message(conn,chat_id)
            if last_message == 'Share my Thought' or  last_message == 'Share another Thought' or  last_message == 'Enter again':
                DBHelper.add_message(conn, content, chat_id, msgid) 
                bot.sendMessage(chat_id, 'Please confirm to share this message :D', reply_markup=keyboard2)
            if last_message == 'I want to reply':
                reply = DBHelper.get_reply(conn,chat_id)
                bot.sendMessage(reply[0],"Some one has just replied your message:\n"+reply[1])
                bot.sendMessage(reply[0],"The reply is:\n"+content,reply_markup = keyboard)
                bot.sendMessage(chat_id, 'Your reply message has been sent. Thank you!!!', reply_markup=reply_keyboard3)
        DBHelper.add_log(conn,content,chat_id, msgid)
        
    


MessageLoop(bot, conversation).run_as_thread()

while 1:
    time.sleep(10)


















