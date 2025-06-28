import pyodbc
import os
import logging
import traceback

def get_connection():
    try:
        conn_str = os.getenv("SQLCONNSTR_SQL_CONNECTION_STRING")
        return pyodbc.connect(conn_str)
    except Exception as e:
        logging.error("Failed to establish DB connection.")
        logging.error(f"Error: {e}")
        logging.error("Stack trace:\n" + traceback.format_exc())
        raise  # Re-raise the exception after logging it