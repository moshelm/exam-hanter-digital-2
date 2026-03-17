import mysql.connector
from mysql.connector import MySQLConnection


def execute_query(conn:MySQLConnection,query:str):
    try:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            return list(cursor.fetchall())
    except Exception:
        raise 


def quality_targets_movement_alert():
    query = """SELECT entity_id,target_name,priority_level,movement_distance_km FROM targets 
    WHERE priority_level IN (1,2) AND movement_distance_km > 5 ;"""
    return query

def process_intel_sources():
    query = """SELECT signal_type, COUNT(signal_type) as total_signals FROM intel_signals 
GROUP BY signal_type ORDER BY total_signals DESC"""
    return query

def detection_new_targets():
    query = """SELECT entity_id, count(*) as reported_number 
    FROM (select * from intel_signals 
    where entity_id like '%UNKNOWN%' OR priority_level = 99) as unknown_e 
    group by entity_id ORDER BY reported_number DESC LIMIT 3"""
    return query

def identification_strange_movement():
    query = """select entity_id from ( SELECT entity_id , date(created_at) as date_day FROM intel_signals
where hour(created_at) > 8 and HOUR(created_at) < 20
group by entity_id, DATE(created_at) 
HAVING MAX(reported_lat) = MIN(reported_lat) and MAX(reported_lon) = MIN(
reported_lon)) as day_static 
join (SELECT entity_id , date(created_at) as date_day FROM intel_signals
where hour(created_at) <= 8 and HOUR(created_at) >= 20
group by entity_id, DATE(created_at) 
HAVING distance_from_last > 10 ) as night_move 
on day_static.entity_id = night_move.entity_id and day_static.date_day=night_move.as date_day) as result """
    return query
