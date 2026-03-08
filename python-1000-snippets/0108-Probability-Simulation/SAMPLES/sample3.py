# sample3.py
# Continuous probability: approximate area under normal curve using direct sampling

import random

# use built-in gaussian generator

def approximate_area(mean, std, low, high, trials):
    count = 0
    for _ in range(trials):
        x = random.gauss(mean, std)
        if low <= x <= high:
            count += 1
    return count / trials

if __name__ == '__main__':
    random.seed(2)
    print('approx area between -1 and 1 for standard normal', approximate_area(0,1,-1,1,100000))
