# sample3.py
# Demonstrate handling an expired JWT (ExpiredSignatureError).

import time

import jwt


def main():
    secret = 'this-is-a-longer-secret-key-at-least-32-bytes'

    payload = {
        'sub': 'user123',
        'iat': int(time.time()) - 120,
        'exp': int(time.time()) - 60,  # already expired
    }

    token = jwt.encode(payload, secret, algorithm='HS256')
    print('Expired token:', token)

    try:
        jwt.decode(token, secret, algorithms=['HS256'])
        print('Token is valid (unexpected)')
    except jwt.ExpiredSignatureError as exc:
        print('Token expired (expected):', exc)


if __name__ == '__main__':
    main()
