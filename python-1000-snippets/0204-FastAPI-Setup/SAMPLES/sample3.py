# sample3.py
# demonstrate automatic OpenAPI docs using TestClient to fetch docs
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get('/ping')
def ping():
    return {'pong': True}

if __name__ == '__main__':
    client = TestClient(app)
    docs = client.get('/docs')
    print('docs status', docs.status_code)
    openapi = client.get('/openapi.json')
    print('openapi keys', list(openapi.json().keys()))
