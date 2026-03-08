# sample3.py
# random initial state and rule comparison

import random

def cellular_automata(initial_state, rule, steps):
    def apply_rule(left, center, right):
        binary = (left << 2) | (center << 1) | right
        return (rule >> binary) & 1

    state = initial_state
    history = [state]
    for _ in range(steps):
        new_state = []
        for i in range(len(state)):
            left = state[i-1] if i > 0 else 0
            right = state[i+1] if i < len(state)-1 else 0
            new_state.append(apply_rule(left, state[i], right))
        state = new_state
        history.append(state)
    return history

if __name__ == '__main__':
    init = [random.randint(0,1) for _ in range(7)]
    print('init', init)
    print('rule 90', cellular_automata(init, 90, 3))
    print('rule 30', cellular_automata(init, 30, 3))
