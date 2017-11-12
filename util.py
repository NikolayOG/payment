import sqlite3
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite")

def get_transactions_db(include_id = False):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    responseData = []
    if include_id:
        for row in c.execute("SELECT date, merchant, amount, charge, total, id FROM transactions"):
            data = dict(zip(['date', 'merchant', 'amount', 'charge', 'total', 'id'], row))
            responseData.append(data)
    else:
        for row in c.execute("SELECT date, merchant, amount, charge, total, fraud FROM transactions"):
            data = dict(zip(['date', 'merchant', 'amount', 'charge', 'total', 'fraud'], row))
            responseData.append(data)
    c.close()
    return responseData