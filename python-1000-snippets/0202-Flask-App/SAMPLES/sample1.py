# sample1.py
# minimal Flask application and using test_client to exercise routes
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    # use the test client so no server needs to run
    with app.test_client() as client:
        resp = client.get('/')
        print('GET / ->', resp.data.decode())
