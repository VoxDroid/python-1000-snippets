# sample3.py
# Ensemble average displacement over multiple 1D walks

import random

def single_walk(steps):
    pos=0
    for _ in range(steps):
        pos += random.choice([-1,1])
    return pos

def ensemble_mean(steps, trials):
    total=0
    for _ in range(trials):
        total += single_walk(steps)
    return total / trials

if __name__ == '__main__':
    random.seed(2)
    print('mean displacement', ensemble_mean(100,1000))
