# sample2.py
# Simulate rolling a six-sided die 10 times.

import random

def roll_dice(n):
    rolls = []
    for _ in range(n):
        rolls.append(random.randint(1, 6))
    return rolls

if __name__ == '__main__':
    print(roll_dice(10))

