# sample1.py
# Basic circuit breaker implementation.

class CircuitBreaker:
    def __init__(self, max_failures=3):
        self.failures = 0
        self.max_failures = max_failures
        self.open = False

    def call(self, func):
        if self.open:
            return 'Circuit open'
        try:
            result = func()
            self.failures = 0
            return result
        except Exception:
            self.failures += 1
            if self.failures >= self.max_failures:
                self.open = True
            return 'Failure'


if __name__ == '__main__':
    cb = CircuitBreaker(max_failures=2)
    print(cb.call(lambda: 1/0))
    print(cb.call(lambda: 1/0))
    print(cb.call(lambda: 1))
