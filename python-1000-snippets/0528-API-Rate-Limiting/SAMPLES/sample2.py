# sample2.py
# Simulate API calls and track over-limit events.


def simulate_requests(limiter, total):
    denied = 0
    for i in range(total):
        if not limiter.allow():
            denied += 1
    return denied


if __name__ == '__main__':
    from sample1 import RateLimiter
    limiter = RateLimiter(2, 4)
    denied = simulate_requests(limiter, 10)
    print('Denied requests:', denied)
