# sample2.py
# Simulate drawing colored balls from an urn without replacement

import random

def urn_simulation(success_color, draws, trials):
    colors = ['red']*5 + ['blue']*3 + ['green']*2
    count=0
    for _ in range(trials):
        draw = random.sample(colors, draws)
        if success_color in draw:
            count+=1
    return count/trials

if __name__ == '__main__':
    random.seed(1)
    print('prob red in 3 draws', urn_simulation('red',3,10000))
