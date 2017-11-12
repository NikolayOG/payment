from flask import Flask, request
import sqlite3
import os.path

import util

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite")

@app.route('/transactions',  methods=['GET'])
def get_transactions():
    responseData = util.get_transactions_db()
    return str(responseData)


@app.route('/transactions', methods=['POST'])
def add_transaction():
    date = request.form["date"]
    merchant = request.form["merchant"]
    amount = request.form["amount"]
    charge = request.form["charge"]
    total = request.form["total"]

    t = (date, merchant, amount, charge, total)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('INSERT INTO transactions(date, merchant, amount, charge, total) VALUES(?, ?, ?, ?, ?)', t)
    conn.commit()
    c.close()
    return "OK"

if __name__ == '__main__':
    app.run()
