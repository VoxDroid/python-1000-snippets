# sample1.py
# Roll a six-sided die three times with seeded randomness

import random

def roll_dice(sides, rolls):
    return [random.randint(1, sides) for _ in range(rolls)]

if __name__ == '__main__':
    random.seed(42)
    print('rolled:', roll_dice(6, 3))
