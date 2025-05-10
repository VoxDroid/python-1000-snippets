# Cellular Automata

## Description
This snippet implements a 1D cellular automaton with a simple rule (e.g., Rule 30) for binary states.

## Code
```python
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

initial_state = [0, 0, 1, 0, 0]
rule = 30
result = cellular_automata(initial_state, rule, 3)
for row in result:
    print(row)
```

## Output
```
[0, 0, 1, 0, 0]
[0, 1, 1, 1, 0]
[1, 1, 0, 0, 1]
[0, 0, 1, 1, 0]
```

## Explanation
- **Cellular Automata**: Evolves a 1D array based on a rule (e.g., Rule 30) mapping neighbor triplets to new states.
- **Rule 30**: Defined by a binary number (30 = 00011110); each triplet maps to a bit.
- **Complexity**: O(n * steps) time, where n is state length.
- **Use Case**: Used in pattern generation or complexity studies.
- **Best Practice**: Visualize output; experiment with different rules.