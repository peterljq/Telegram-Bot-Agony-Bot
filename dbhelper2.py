import python_mysql_connect2
from mysql.connector import Error
import random
class DBHelper:
    conn = python_mysql_connect2.connect()
    def add_log(content, sender, msgid):
        query = "INSERT INTO log(content, sender,id) " \
            "VALUES(%s,%s,%s)"
        args = (content, sender, msgid)
        try:
            print("inserting a new message...")
            cursor = self.conn.cursor()
            cursor.execute(query,args)
            conn.commit()
        except Error as err:
            print(err.msg)
        cursor.close()
        
    def add_message(description, sender, msgid):
        query = "INSERT INTO agony(description,sender,num_like, id) " \
            "VALUES(%s,%s,%s,%s)"
        args = (description, sender, 0,msgid)
        try:
            print("inserting a new message...")
            cursor = conn.cursor()
            cursor.execute(query,args)
            conn.commit()
        except Error as err:
            print(err.msg)
        cursor.close()

    def add_reply(message,reply,msgid,sender,replyid):
        query = "INSERT INTO aunt(message,reply,msgid,sender,replyid) " \
            "VALUES(%s,%s,%s,%s,%s)"
        args = (message,reply,msgid,sender,replyid)
        try:
            print("inserting a new reply..")
            cursor = conn.cursor()
            cursor.execute(query,args)
            self.conn.commit()
        except Error as err:
            print(err.msg)
        cursor.close()

    def get_last_message(sender):
        query = "select content from log where sender =%s order by id desc"
        args = (sender,)
        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            result = self.cursor.fetchall()
        except Error as err:
            print(err)
        cursor.close()
        return result[0][0]
    
    def get_message(sender):
        query = "select description, sender,id from agony where sender !=%s;"
        args = (sender,)
        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            row = cursor.fetchall()
            n = random.randint(0,cursor.rowcount-1)
            result = row[n]
        except Error as err:
            print(err)
        cursor.close()
        return result

    def last_sent_message(sender):
        query = "select id from agony where sender = %s;"
        args = (sender,)
        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            row = cursor.fetchall()
            n = cursor.rowcount - 1
            result = row[n][0]
        except Error as err:
            print(err)
        cursor.close()
        return result
    
    def delete_message(msgid):
        query = "delete from agony where id = %s;"
        args = (msgid, )
        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
        except Error as err:
            print(err)
        cursor.close()

    def get_reply(sender):
        query = "select sender, message, msgid from aunt where replyid =%s;"
        args = (sender,)
        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            result = cursor.fetchall()
        except Error as err:
            print(err)
        cursor.close()
        return result[-1]
    
    def increase_like(msgid):
        query = """ UPDATE agony
                SET num_like = num_like+1
                WHERE id = %s """
        args = (msgid, )
        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
        except Error as err:
            print(err)
        cursor.close()

    def mark_as_spam(msgid):
        query = """UPDATE agony
                SET spam = true
                where id = %s """
        args = (msgid, )
        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
        except Error as err:
            print(err)
        cursor.close()
        
    def get_like(msgid):
        query = "select num_like from agony where id = %s"
        args = (msgid, )
        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            result = cursor.fetchall()
        except Error as err:
            print(err)
        cursor.close()
        return result[0][0]

    
