# sample1.py
# Simulate simple 2-state Markov chain

import random

transition_matrix = {
    'A': {'A': 0.7, 'B': 0.3},
    'B': {'A': 0.4, 'B': 0.6}
}

def markov_chain(start_state, steps):
    current = start_state
    sequence = [current]
    for _ in range(steps):
        probs = transition_matrix[current]
        next_state = random.choices(list(probs.keys()), list(probs.values()))[0]
        sequence.append(next_state)
        current = next_state
    return sequence

if __name__ == '__main__':
    random.seed(0)
    print('chain', markov_chain('A',5))
