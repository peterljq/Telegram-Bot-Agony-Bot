TOKEN = '406823099:AAEedgrkGSbHl0mWOq5wowluQ088EREb8QE'
import time
import telepot
from dbhelper1 import DBHelper
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup

bot = telepot.Bot(TOKEN)

admin_keyboard1 = ReplyKeyboardMarkup(keyboard = [['Post message to all users'], ['Fetch top 10 favorite messages'], ['Send favorite messages to all users']], one_time_keyboard = True, resize_keyboard=True)
confirm_keyboard1 = ReplyKeyboardMarkup(keyboard = [['Confirm Posting'],['Re-enter the massage']], one_time_keyboard = True, resize_keyboard = True)
confirm_keyboard2 = ReplyKeyboardMarkup(keyboard = [['Confirm Sending'],['Cancel']])
def conversation(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    content = msg['text']

    if content_type == 'text' and content == ('/admin' or 'Cancel') and chat_id == :       # 在chat——id后面填上我们几个人的ID PS:chatid就是用户的id吧 我忘记了
        bot.sendMessage(chat_id, text='Welcome, you are an admin. Please select from the following functions', reply_markup=admin_keyboard1)
    elif content_type == 'text' and content == ('Post message to all user' or 'Re-enter the message') and chat_id == :
        bot.sendMessage(chat_id, text='Your next message will be sent to all users', reply_markup=confirm_keyboard1)
    elif content_type == 'text' and content == 'Fetch top 10 favorite messages' and chat_id == :
        bot.sendMessage(chat_id, text='', reply_markup=admin_keyboard1) # text后面加上获取的top 10 messages
    elif content_type == 'text' and content == 'Send favorite messages to all users' and chat_id == :
        bot.sendMessage(chat_id, text='Please confirm sending', reply_markup=confirm_keyboard2)
    elif content_type == 'text' and content == 'Confirm Posing' and chat_id == :
        # 这一行加上bot给所有人发消息的指令， 消息的内容为post message to all user之后的消息
        bot.sendMessage(chat_id, text='The message has been sent', reply_markup=admin_keyboard1)
    elif content_type == 'text' and content == 'Confirm Sending' and chat_id == :
        # 这一行加上bot给所有人发送top 10 messages
        bot.sendMessage(chat_id, text = 'Top 10 message has been sent to all users', reply_markup=admin_keyboard1)




MessageLoop(bot, conversation).run_as_thread()

while 1:
    time.sleep(10)
