# sample1.py
# Simple 1D random walk

import random

def random_walk(steps):
    position = 0
    positions = [position]
    for _ in range(steps):
        position += random.choice([-1, 1])
        positions.append(position)
    return positions

if __name__ == '__main__':
    random.seed(0)
    print('walk', random_walk(10))
