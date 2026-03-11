# sample1.py
# simple FastAPI app with one endpoint and test client
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'hello'}

if __name__ == '__main__':
    client = TestClient(app)
    resp = client.get('/')
    print('GET / ->', resp.status_code, resp.json())
