from fastapi import APIRouter,Request,Depends
from mysql.connector import MySQLConnection
from dal import *
router = APIRouter()
def get_connection(request:Request):
    return request.app.stat.conn_mysql

@router.get('/query_1',status_code=200)
def query_1_res(conn: MySQLConnection = Depends(get_connection)):
    return execute_query(conn,query_1())
