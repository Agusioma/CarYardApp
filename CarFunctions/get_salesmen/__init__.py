import azure.functions as func
from shared.db import get_connection

def main(req: func.HttpRequest) -> func.HttpResponse:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Name, Email FROM Salesmen")
    rows = cursor.fetchall()
    result = [{"name": r[0], "email": r[1]} for r in rows]
    return func.HttpResponse(str(result), mimetype="application/json")
