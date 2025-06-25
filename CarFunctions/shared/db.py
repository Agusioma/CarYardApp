import pyodbc
import os

def get_connection():
    conn_str = os.getenv("SQL_CONNECTION_STRING")
    return pyodbc.connect(conn_str)
