# sample2.py
# Demonstrate circuit breaker reset after timeout (simple simulation).

import time
from sample1 import CircuitBreaker


if __name__ == '__main__':
    cb = CircuitBreaker(max_failures=1)
    print('first call:', cb.call(lambda: 1/0))
    print('second call after fail:', cb.call(lambda: 1))
    # simple reset behavior
    time.sleep(0.1)
    cb.open = False
    cb.failures = 0
    print('after reset, call success:', cb.call(lambda: 1))
