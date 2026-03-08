# sample2.py
# Use numpy vectorization for faster simulation

import numpy as np

def estimate_pi_np(trials):
    x = np.random.uniform(-1,1,size=trials)
    y = np.random.uniform(-1,1,size=trials)
    inside = np.sum(x*x + y*y <=1)
    return 4 * inside / trials

if __name__ == '__main__':
    np.random.seed(1)
    print('pi approx numpy', estimate_pi_np(1000000))
