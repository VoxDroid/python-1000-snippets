# Markov Chain

## Description
This snippet simulates a Markov chain to generate a sequence of states based on transition probabilities.

## Code
```python
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

print("Markov Chain:", markov_chain('A', 5))
```

## Output
```
Markov Chain: ['A', 'A', 'B', 'B', 'A', 'A']
```
*(Output varies due to randomness)*

## Explanation
- **Markov Chain**: A stochastic model where the next state depends only on the current state, defined by a transition matrix.
- **Logic**: Uses `random.choices` to select the next state based on probabilities.
- **Complexity**: O(steps) time.
- **Use Case**: Used in text generation, weather modeling, or financial simulations.
- **Best Practice**: Validate transition probabilities sum to 1; use for small state spaces.