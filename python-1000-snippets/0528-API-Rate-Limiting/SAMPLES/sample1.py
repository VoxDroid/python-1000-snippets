# sample1.py
# Basic token bucket rate limiter.

import time


class RateLimiter:
    def __init__(self, rate_per_sec, burst):
        self.rate = rate_per_sec
        self.capacity = burst
        self.tokens = burst
        self.last = time.time()

    def allow(self):
        now = time.time()
        elapsed = now - self.last
        self.last = now
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False


if __name__ == '__main__':
    limiter = RateLimiter(1, 3)
    for i in range(5):
        print(f'Request {i} allowed:', limiter.allow())
        time.sleep(0.2)
