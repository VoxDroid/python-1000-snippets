# sample1.py
# perform a simple GET and print name field

import requests

if __name__ == '__main__':
    try:
        r = requests.get('https://jsonplaceholder.typicode.com/users/1', timeout=3)
        r.raise_for_status()
        user = r.json()
        print('name', user.get('name'))
    except requests.RequestException as e:
        print('request failed', e)
