# sample2.py
# Show failure when decoding a JWT with the wrong secret.

import time

import jwt


def main():
    secret = 'this-is-a-longer-secret-key-at-least-32-bytes'
    wrong_secret = 'this-is-a-different-long-secret-key-for-invalid-test'

    payload = {
        'sub': 'user123',
        'iat': int(time.time()),
        'exp': int(time.time()) + 60,
    }

    token = jwt.encode(payload, secret, algorithm='HS256')
    print('Token:', token)

    try:
        jwt.decode(token, wrong_secret, algorithms=['HS256'])
        print('Decoded with wrong key (unexpected)')
    except jwt.InvalidSignatureError as exc:
        print('Invalid signature (expected):', exc)


if __name__ == '__main__':
    main()
