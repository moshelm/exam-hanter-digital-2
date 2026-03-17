import mysql.connector
from mysql.connector import MySQLConnection
import os 

mysql_host = os.getenv("MYSQL_HOST",'mysql')
mysql_port = int(os.getenv("MYSQL_PORT",'3306'))
mysql_user = os.getenv("MYSQL_USER",'root')
mysql_password = os.getenv("MYSQL_PASSWORD",'root')
mysql_database = os.getenv("MYSQL_DATABASE",'digital_hunter')

def connect()->MySQLConnection:
    try:
        client = mysql.connector.connect(host=mysql_host,port=mysql_port,user=mysql_user,
                                        password=mysql_password,database=mysql_database)
        return client
    except mysql.connector.Error as e:
        print('hi',e)