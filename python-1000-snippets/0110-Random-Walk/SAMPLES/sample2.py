# sample2.py
# 2D random walk simulation

import random

def random_walk_2d(steps):
    x,y = 0,0
    path=[(x,y)]
    for _ in range(steps):
        dx,dy = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        x += dx; y += dy
        path.append((x,y))
    return path

if __name__ == '__main__':
    random.seed(1)
    print('2D path', random_walk_2d(10))
