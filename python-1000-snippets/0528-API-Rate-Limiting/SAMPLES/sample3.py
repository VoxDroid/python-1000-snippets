# sample3.py
# Log rate limit violations to temp file.

import os
from sample1 import RateLimiter

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0528_rate_limit_violations.log')


def run_and_log(limiter, requests):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'a') as f:
        for i in range(requests):
            if not limiter.allow():
                f.write(f'request {i} denied\n')


if __name__ == '__main__':
    limiter = RateLimiter(1, 2)
    run_and_log(limiter, 5)
    print('Logged rate limit violations to', OUTPUT_PATH)
