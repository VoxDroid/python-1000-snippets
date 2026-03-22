# sample2.py
# Lifecycle: create, refresh, expire session objects.

import time


def create_session(user_id, ttl_seconds=5):
    return {'user_id': user_id, 'created': time.time(), 'expires': time.time() + ttl_seconds}


def is_valid(session):
    return time.time() < session['expires']


if __name__ == '__main__':
    sess = create_session('user2', ttl_seconds=1)
    print('Valid initially:', is_valid(sess))
    time.sleep(1.1)
    print('Valid after ttl:', is_valid(sess))
