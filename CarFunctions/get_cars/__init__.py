import azure.functions as func
from shared.db import get_connection

def main(req: func.HttpRequest) -> func.HttpResponse:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Make, Model, Year, Price FROM Cars")
    rows = cursor.fetchall()
    result = [{"make": r[0], "model": r[1], "year": r[2], "price": float(r[3])} for r in rows]
    return func.HttpResponse(str(result), mimetype="application/json")
