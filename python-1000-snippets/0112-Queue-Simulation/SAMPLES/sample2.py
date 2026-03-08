# sample2.py
# Use deque for efficient queue and track average queue length

import random
from collections import deque

def queue_sim(arrival_rate, service_rate, time_steps):
    queue = deque()
    wait_times=[]
    queue_lengths=[]
    serving_until=0
    for t in range(time_steps):
        if random.random() < arrival_rate:
            queue.append(t)
        queue_lengths.append(len(queue))
        if t>=serving_until and queue:
            arrival_time = queue.popleft()
            wait_times.append(t-arrival_time)
            serving_until = t + random.expovariate(service_rate)
    return (sum(wait_times)/len(wait_times) if wait_times else 0,
            sum(queue_lengths)/len(queue_lengths))

if __name__ == '__main__':
    random.seed(1)
    print(queue_sim(0.2,0.3,1000))
