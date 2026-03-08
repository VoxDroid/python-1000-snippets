# sample1.py
# Estimate probability of rolling a 7 with two dice

import random

def dice_probability(target_sum, trials):
    count = 0
    for _ in range(trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == target_sum:
            count += 1
    return count / trials

if __name__ == '__main__':
    random.seed(0)
    print('prob', dice_probability(7, 10000))
