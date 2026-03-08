# sample1.py
# rule 30 on a simple seed

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
    print(cellular_automata([0,0,1,0,0], 30, 3))
