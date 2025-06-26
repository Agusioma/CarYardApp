import azure.functions as func
import logging
from shared.db import get_connection

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("START: get_salesmen function invoked")
    try:
        conn = get_connection()
        logging.info("Connected to DB")
        cursor = conn.cursor()
        cursor.execute("SELECT Name, Email FROM dbo.Salesmen")
        rows = cursor.fetchall()
        result = [{"name": r[0], "email": r[1]} for r in rows]
        return func.HttpResponse(str(result), mimetype="application/json")
    except Exception as e:
        logging.error(f"ERROR in get_salesmen: {str(e)}")
        return func.HttpResponse(f"ERROR in get_salesmen: {str(e)}", status_code=500)