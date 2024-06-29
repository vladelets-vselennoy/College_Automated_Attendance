import pandas as pd
from datetime import datetime, timedelta
import psycopg2
from connection import get_db_connection

DB_PARAMS = {
    "dbname": "autoattendance",
    "user": "postgres",
    "password": "Postgre",
    "host": "localhost"
}

# def get_db_connection():
#     return psycopg2.connect(**DB_PARAMS)
def generate_daily_report(date):
    conn = get_db_connection()
    query = """
    SELECT s.name, sub.name as subject, a.date
    FROM attendance a
   
    JOIN student s ON a.student_id = s.std_id
    JOIN subject sub ON a.subject_id = sub.sub_id
    WHERE a.date = %s
    ORDER BY sub.name, s.name
    """
    df = pd.read_sql_query(query, conn, params=(date,))
    # conn.close()
    return df

def generate_weekly_report(start_date, end_date):
    conn = get_db_connection()
    query = """
    SELECT s.name, sub.name as subject, COUNT(a.date) as days_present
    FROM attendance a
    JOIN student s ON a.student_id = s.std_id
    JOIN subject sub ON a.subject_id = sub.sub_id
    WHERE a.date BETWEEN %s AND %s
    GROUP BY s.name, sub.name
    ORDER BY sub.name, s.name
    """
    df = pd.read_sql_query(query, conn, params=(start_date, end_date))
    # conn.close()
    return df

def generate_monthly_report(year, month):
    conn = get_db_connection()
    query = """
    SELECT s.name, sub.name as subject, COUNT(a.date) as days_present
    FROM attendance a
    JOIN student s ON a.student_id = s.std_id
    JOIN subject sub ON a.subject_id = sub.sub_id
    WHERE EXTRACT(YEAR FROM a.date) = %s AND EXTRACT(MONTH FROM a.date) = %s
    GROUP BY s.name, sub.name
    ORDER BY sub.name, s.name
    """
    df = pd.read_sql_query(query, conn, params=(year, month))
    # conn.close()
    return df