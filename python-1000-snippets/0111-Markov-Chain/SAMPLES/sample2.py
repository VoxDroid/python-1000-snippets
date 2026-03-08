# sample2.py
# Estimate stationary distribution by simulation

import random

def simulate(trans, start, steps):
    state = start
    counts = {s:0 for s in trans}
    for _ in range(steps):
        counts[state] += 1
        probs = trans[state]
        state = random.choices(list(probs.keys()), list(probs.values()))[0]
    return {s:counts[s]/steps for s in counts}

if __name__ == '__main__':
    random.seed(1)
    trans = {
        'A':{'A':0.9,'B':0.1},
        'B':{'A':0.5,'B':0.5}
    }
    print('stationary approx', simulate(trans,'A',100000))
