# sample2.py
# POST JSON payload and check response
import requests

if __name__ == '__main__':
    payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
    resp = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload, timeout=5)
    resp.raise_for_status()
    data = resp.json()
    print('Created ID:', data.get('id'))

