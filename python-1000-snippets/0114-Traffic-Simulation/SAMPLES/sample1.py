# sample1.py
# single deterministic run with a fixed seed

import random

def traffic_simulation(cycles, arrival_rate, green_duration=10, cars_per_green=2, seed=None):
    if seed is not None:
        random.seed(seed)
    cars_waiting = 0
    total_wait_time = 0
    green = True
    for t in range(cycles):
        if random.random() < arrival_rate:
            cars_waiting += 1
        if t % green_duration == 0:
            green = not green
        if not green:
            total_wait_time += cars_waiting
        elif green and cars_waiting > 0:
            cars_waiting -= min(cars_waiting, cars_per_green)
    return total_wait_time / cycles

if __name__ == '__main__':
    avg_wait = traffic_simulation(100, 0.3, seed=42)
    print('avg wait', avg_wait)
