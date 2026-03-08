# sample3.py
# Parallel Monte Carlo simulation using multiprocessing

import random
from multiprocessing import Pool

def worker(trials):
    count=0
    for _ in range(trials):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        if x*x+y*y<=1:
            count+=1
    return count

if __name__ == '__main__':
    total_trials = 1000000
    processes = 4
    with Pool(processes) as pool:
        counts = pool.map(worker, [total_trials//processes]*processes)
    pi_est = 4 * sum(counts) / total_trials
    print('pi parallel approx', pi_est)
