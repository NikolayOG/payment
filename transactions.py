from web import app


@app.route('/transactions')
def get_transactions():
    return 'OK'