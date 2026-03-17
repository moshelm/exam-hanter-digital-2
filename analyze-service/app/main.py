from fastapi import FastAPI
from contextlib import asynccontextmanager
from mysql_connection import connect
from routes import router

@asynccontextmanager
async def lifespan(app:FastAPI):
        conn_mysql = connect()
        app.state.conn_mysql = connect()
        yield
        conn_mysql.close()
        
app = FastAPI(lifespan=lifespan)
app.include_router(router)