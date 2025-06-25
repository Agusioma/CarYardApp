import azure.functions as func
import logging
from shared.db import get_connection

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("START: get_cars function invoked")
    try:
        conn = get_connection()
        logging.info("Connected to DB")
        cursor = conn.cursor()
        cursor.execute("SELECT Make, Model, Year, Price FROM Cars")
        rows = cursor.fetchall()
        result = [{"make": r[0], "model": r[1], "year": r[2], "price": float(r[3])} for r in rows]
        return func.HttpResponse(str(result), mimetype="application/json")
    except Exception as e:
        logging.error(f"ERROR in get_cars: {str(e)}")
        return func.HttpResponse(f"ERROR in get_cars: {str(e)}", status_code=500)

