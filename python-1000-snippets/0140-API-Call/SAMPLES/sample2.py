# sample2.py
# make a POST request with JSON payload

import requests

if __name__ == '__main__':
    try:
        payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
        r = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload, timeout=3)
        r.raise_for_status()
        print('created', r.json())
    except requests.RequestException as e:
        print('post failed', e)
