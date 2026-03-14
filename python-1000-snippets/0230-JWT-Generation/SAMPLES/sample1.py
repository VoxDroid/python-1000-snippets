# sample1.py
# Generate and validate a JWT using a symmetric secret (HS256).

import time

import jwt


def main():
    secret = 'this-is-a-longer-secret-key-at-least-32-bytes'

    payload = {
        'sub': 'user123',
        'role': 'admin',
        'iat': int(time.time()),
        'exp': int(time.time()) + 60,  # expires in 60 seconds
    }

    token = jwt.encode(payload, secret, algorithm='HS256')
    print('JWT:', token)

    # Validate and decode
    decoded = jwt.decode(token, secret, algorithms=['HS256'])
    print('Decoded claims:', decoded)


if __name__ == '__main__':
    main()
