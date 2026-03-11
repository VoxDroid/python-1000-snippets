# sample2.py
# demonstrate form submission using Flask test client
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        return 'Hello, ' + request.form.get('name', 'Guest')
    return '<form method="post"><input name="name"><input type="submit"></form>'

if __name__ == '__main__':
    with app.test_client() as client:
        r1 = client.get('/')
        print('GET / ->', r1.data.decode())
        r2 = client.post('/', data={'name': 'Tester'})
        print('POST / ->', r2.data.decode())
