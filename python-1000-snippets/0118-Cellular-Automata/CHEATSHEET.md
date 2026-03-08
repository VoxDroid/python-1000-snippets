# 0118-Cellular-Automata Cheatsheet

- **Purpose**: evolve a 1D binary array according to a Wolfram rule (0–255).
- **Usage**: `cellular_automata(initial_state, rule, steps)` returns history list.

```python
from cellular_automata import cellular_automata

print(cellular_automata([0,0,1,0,0], 30, 3))  # rule 30
print(cellular_automata([1,0,1,0,1], 110, 5))
```

- Rule number encodes output bits for patterns 111,110,…,000.
- Common rules: 30 (chaotic), 90 (XOR), 110 (Turing‑complete).
- Visualize history with `print('\n'.join(''.join(str(x) for x in row) for row in hist))`.
- Experiment with random initial states: `[random.randint(0,1) for _ in range(n)]`.

