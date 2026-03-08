# sample1.py
# Estimate pi using Monte Carlo

import random

def estimate_pi(trials):
    inside = 0
    for _ in range(trials):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x*x + y*y <= 1:
            inside += 1
    return 4 * inside / trials

if __name__ == '__main__':
    random.seed(0)
    print('pi approx', estimate_pi(100000))
