import pyodbc
import os
import logging
import traceback

def get_connection():
    try:
        conn_str = os.getenv("SQLCONNSTR_SQL_CONNECTION_STRING")
        logging.info("🔍 Environment Variables:")
        for key, value in os.environ.items():
            logging.info(f"{key} = {value}")
        logging.info(conn_str)
        '''if not conn_str:
            raise ValueError("SQL_CONNECTION_STRING is not set in environment variables.")'''
        return pyodbc.connect(conn_str)
    except Exception as e:
        logging.error("Failed to establish DB connection.")
        logging.error(f"Error: {e}")
        logging.error("Stack trace:\n" + traceback.format_exc())
        raise  # Re-raise the exception after logging it
