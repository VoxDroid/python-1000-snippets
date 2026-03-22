# sample3.py
# Log circuit breaker state transitions to temp.

import os
from sample1 import CircuitBreaker

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0529_circuit_log.txt')


def log_state(message):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'a') as f:
        f.write(message + '\n')


if __name__ == '__main__':
    cb = CircuitBreaker(max_failures=2)

    for fn in [lambda: 1/0, lambda: 1/0, lambda: 1]:
        res = cb.call(fn)
        log_state(f'Result: {res}, failures: {cb.failures}, open: {cb.open}')

    print('Circuit log written to', OUTPUT_PATH)
