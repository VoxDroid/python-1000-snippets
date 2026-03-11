# sample3.py
# demonstrate error handler
from flask import Flask, abort

app = Flask(__name__)

@app.route('/error')
def error():
    abort(404)

@app.errorhandler(404)
def not_found(e):
    return 'Custom 404', 404

if __name__ == '__main__':
    with app.test_client() as client:
        r = client.get('/error')
        print('GET /error ->', r.status_code, r.data.decode())
