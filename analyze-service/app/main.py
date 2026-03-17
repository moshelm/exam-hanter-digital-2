from fastapi import FastAPI
from contextlib import asynccontextmanager
from mysql_connection import connect
from routes import router
import time

@asynccontextmanager
async def lifespan(app:FastAPI):

        retry = 10
        while retry !=0:
                conn_mysql = connect()
                app.state.conn_mysql = conn_mysql
                if conn_mysql:
                        break
                else:
                        retry -= 1
                        time.sleep(2)
        yield
        conn_mysql.close()
        
app = FastAPI(lifespan=lifespan)
app.include_router(router)