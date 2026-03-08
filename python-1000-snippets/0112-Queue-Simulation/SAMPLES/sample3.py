# sample3.py
# Parallel simulation of many independent single-server queues

import random
from multiprocessing import Pool

def simulate_one(args):
    arrival_rate, service_rate, time_steps = args
    queue=[]
    wait_times=[]
    serving_until=0
    for t in range(time_steps):
        if random.random() < arrival_rate:
            queue.append(t)
        if t>=serving_until and queue:
            arrival = queue.pop(0)
            wait_times.append(t-arrival)
            serving_until = t + random.expovariate(service_rate)
    return sum(wait_times)/len(wait_times) if wait_times else 0

if __name__ == '__main__':
    total = 0
    trials = 5
    with Pool(2) as pool:
        results = pool.map(simulate_one, [(0.1,0.2,1000)]*trials)
    print('parallel waits', results)
