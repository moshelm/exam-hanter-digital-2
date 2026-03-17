from fastapi import APIRouter,Request,Depends, HTTPException
from mysql.connector import MySQLConnection
from dal import *


router = APIRouter()
def get_connection(request:Request):
    return request.app.state.conn_mysql

@router.get('/quality_targets_movement_alert',status_code=200)
def quality_targets_alert(conn: MySQLConnection = Depends(get_connection)):
    try:
        return {'result':execute_query(conn,quality_targets_movement_alert())}
    except Exception as e:
        raise HTTPException(status_code=400,detail=e)
    

@router.get('/process_intel_sources',status_code=200)
def intel_sources(conn: MySQLConnection = Depends(get_connection)):
    try:
        return {'result':execute_query(conn,process_intel_sources())}
    except Exception as e:
        raise HTTPException(status_code=400,detail=e)
    

@router.get('/detection_new_targets',status_code=200)
def new_targets(conn: MySQLConnection = Depends(get_connection)):
    try:
        return {'result':execute_query(conn,detection_new_targets())}
    except Exception as e:
        raise HTTPException(status_code=400,detail=e)
    

@router.get('/identification_strange_movement',status_code=200)
def strange_movement(conn: MySQLConnection = Depends(get_connection)):
    try:
        return {'result':execute_query(conn,identification_strange_movement())}
    except Exception as e:
        raise HTTPException(status_code=400,detail=e)
    

@router.get('/points_visualization',status_code=200)
def visualization(conn: MySQLConnection = Depends(get_connection)):
    try:
        result = execute_query(conn,vis())
        
    except Exception as e:
        raise HTTPException(status_code=400,detail=e)


    

