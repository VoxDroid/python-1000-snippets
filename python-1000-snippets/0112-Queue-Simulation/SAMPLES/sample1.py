# sample1.py
# Single-server queue simulation

import random

def queue_simulation(arrival_rate, service_rate, time_steps):
    queue = []
    wait_times = []
    serving_until = 0
    for t in range(time_steps):
        if random.random() < arrival_rate:
            queue.append(t)
        if t >= serving_until and queue:
            arrival_time = queue.pop(0)
            wait_times.append(t - arrival_time)
            serving_until = t + random.expovariate(service_rate)
    return sum(wait_times)/len(wait_times) if wait_times else 0

if __name__ == '__main__':
    random.seed(0)
    print('avg wait', queue_simulation(0.1,0.2,1000))
