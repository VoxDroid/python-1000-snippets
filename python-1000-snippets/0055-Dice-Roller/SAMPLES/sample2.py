# sample2.py
# Roll a custom-sided die and count frequencies

import random
from collections import Counter

def roll_dice(sides, rolls):
    return [random.randint(1, sides) for _ in range(rolls)]

if __name__ == '__main__':
    sides = int(input('sides: '))
    rolls = int(input('rolls: '))
    results = roll_dice(sides, rolls)
    print('results:', results)
    print('frequencies:', Counter(results))
