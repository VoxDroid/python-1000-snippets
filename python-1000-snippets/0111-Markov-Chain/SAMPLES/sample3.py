# sample3.py
# Use NumPy for vectorized transitions

import numpy as np

def markov_numpy(P, start_idx, steps):
    num_states = P.shape[0]
    state = start_idx
    seq=[state]
    for _ in range(steps):
        state = np.random.choice(num_states, p=P[state])
        seq.append(state)
    return seq

if __name__ == '__main__':
    np.random.seed(2)
    P = np.array([[0.7,0.3],[0.4,0.6]])
    print('numpy chain', markov_numpy(P,0,5))
