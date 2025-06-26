import pyodbc
import os
import logging
import traceback

def get_connection():
    try:
        conn_str = os.getenv("SQLCONNSTR_SQL_CONNECTION_STRING")

        conn = pyodbc.connect(conn_str)
        logging.info("✅ Successfully connected to the database.")

        cursor = conn.cursor()

        cursor.execute("SELECT DB_NAME()")
        current_db = cursor.fetchone()[0]
        logging.info(f"🧭 Currently using database: {current_db}")

        # List databases
        logging.info("📚 Databases:")
        cursor.execute("SELECT name FROM sys.databases")
        for row in cursor.fetchall():
            logging.info(f"  - {row.name}")

        # Switch to target DB if needed
        # cursor.execute("USE your_database_name")

        # List schemas
        logging.info("📂 Schemas:")
        cursor.execute("SELECT name FROM sys.schemas")
        for row in cursor.fetchall():
            logging.info(f"  - {row.name}")

        # List tables
        logging.info("🧾 Tables:")
        cursor.execute("SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        for row in cursor.fetchall():
            logging.info(f"  - {row.TABLE_SCHEMA}.{row.TABLE_NAME}")

        return conn

    except Exception as e:
        logging.error("❌ Failed to establish DB connection.")
        logging.error(f"Error: {e}")
        logging.error("Stack trace:\n" + traceback.format_exc())
        raise  # Re-raise the exception after logging it
