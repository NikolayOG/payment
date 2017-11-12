import json
import sqlite3
import os.path

from kafka import KafkaConsumer

import fraudService
import util

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite")

consumer = KafkaConsumer('test')
for msg in consumer:
    print(msg.value)
    data = json.loads(msg.value)
    date = data["date"]
    merchant = data["merchant"]
    amount = 0
    try:
        amount = float(data["amount"])
    except ValueError:
        continue
    charge = amount - int(amount)
    if charge > 0.8:
        charge = 1 - charge
    elif 0.5 > charge > 0.30:
        charge = 0.5 - charge
    else:
        charge = 0
    total = charge + amount


    t = (date, merchant, amount, charge, total)
    conn = sqlite3.connect(db_path, isolation_level=None)
    c = conn.cursor()
    c.execute('INSERT INTO transactions(date, merchant, amount, charge, total) VALUES(?, ?, ?, ?, ?)', t)
    conn.commit()
    fraud = fraudService.detect_fraud_json(util.get_transactions_db(include_id=True))
    if fraud[-1][1] == -1:
        c.execute('UPDATE transactions SET fraud = 1 WHERE id = ?', (fraud[-1][0] + 1,))
        conn.commit()
    c.close()

