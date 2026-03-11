# sample2.py
# demonstrate a POST endpoint with Pydantic model
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient

class Item(BaseModel):
    name: str
    price: float

app = FastAPI()

@app.post('/items/')
def create_item(item: Item):
    return {'received': item.dict()}

if __name__ == '__main__':
    client = TestClient(app)
    resp = client.post('/items/', json={'name': 'foo', 'price': 3.14})
    print('POST /items/ ->', resp.status_code, resp.json())
