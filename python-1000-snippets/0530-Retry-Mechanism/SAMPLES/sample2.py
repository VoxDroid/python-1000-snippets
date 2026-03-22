# sample2.py
# Exponential backoff retry loop for requests.

import time


def call_with_retry(action, attempts=4, base_delay=0.05):
    for i in range(attempts):
        try:
            return action()
        except Exception as e:
            if i == attempts - 1:
                return f'Failed: {e}'
            time.sleep(base_delay * (2 ** i))


if __name__ == '__main__':
    counter = {'tries': 0}

    def flaky_action():
        counter['tries'] += 1
        if counter['tries'] < 3:
            raise RuntimeError('transient')
        return 'done'

    print('Call result:', call_with_retry(flaky_action))
