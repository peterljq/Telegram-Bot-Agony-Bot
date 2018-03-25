from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def connect():
	"""Connect to MySQL database"""

	db_config = read_db_config()

	try:
		print('Connection to MySQL database...')
		conn = MySQLConnection(**db_config)

		if conn.is_connected():
			return conn
		else:
			print('connection failed.')
			return null

	except Error as error:
		print(error)

if __name__ == '__main__':
	connect()
