# sample3.py
# Use a Session for connection reuse; handle errors
import requests

if __name__ == '__main__':
    with requests.Session() as session:
        try:
            resp = session.get('https://jsonplaceholder.typicode.com/users', timeout=5)
            resp.raise_for_status()
            users = resp.json()
            print('Users count:', len(users))
        except requests.exceptions.RequestException as e:
            print('Request error:', e)

