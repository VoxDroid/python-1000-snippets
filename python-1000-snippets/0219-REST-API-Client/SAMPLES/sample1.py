# sample1.py
# Simple GET request to a public API
import requests

if __name__ == '__main__':
    resp = requests.get('https://jsonplaceholder.typicode.com/users/1', timeout=5)
    resp.raise_for_status()
    user = resp.json()
    print('User:', user.get('name'))

