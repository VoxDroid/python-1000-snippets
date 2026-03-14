# sample1.py
# Validate a JWT (HS256) and print decoded claims.

import time

import jwt


def main():
    secret = 'this-is-a-longer-secret-key-at-least-32-bytes'

    payload = {
        'sub': 'user123',
        'roles': ['admin'],
        'iat': int(time.time()),
        'exp': int(time.time()) + 60,
    }

    token = jwt.encode(payload, secret, algorithm='HS256')
    print('Token:', token)

    decoded = jwt.decode(token, secret, algorithms=['HS256'])
    print('Decoded claims:', decoded)


if __name__ == '__main__':
    main()
