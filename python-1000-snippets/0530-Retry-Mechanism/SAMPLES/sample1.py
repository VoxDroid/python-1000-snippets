# sample1.py
# Retry decorator with max attempts and delay.

import time


def retry(max_attempts=3, delay=0.1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == max_attempts - 1:
                        return f'Failed: {e}'
                    time.sleep(delay)
            return 'Failed'
        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.05)
def flakey():
    flakey.count = getattr(flakey, 'count', 0) + 1
    if flakey.count < 3:
        raise ValueError('temporary error')
    return 'success'


if __name__ == '__main__':
    print('Retry result:', flakey())
