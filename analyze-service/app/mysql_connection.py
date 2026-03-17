import mysql.connector
from mysql.connector import MySQLConnection
import os 

mysql_host = os.getenv("MYSQL_HOST",'mysql')
mysql_port = int(os.getenv("MYSQL_PORT",'3306'))
mysql_user = os.getenv("MYSQL_USER",'root')
mysql_password = os.getenv("MYSQL_PASSWORD",'root')

def connect()->MySQLConnection:
    client = mysql.connector.connect(host=mysql_host,port=mysql_port,user=mysql_user,
                                     password=mysql_password)
    return client
    