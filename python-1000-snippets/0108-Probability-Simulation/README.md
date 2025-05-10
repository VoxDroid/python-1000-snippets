# Probability Simulation

## Description
This snippet simulates rolling two dice to estimate the probability of a specific sum.

## Code
```python
import random

def dice_probability(target_sum, trials):
    count = 0
    for _ in range(trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == target_sum:
            count += 1
    return count / trials

target_sum = 7
trials = 10000
print(f"Probability of sum {target_sum}: {dice_probability(target_sum, trials):.4f}")
```

## Output
```
Probability of sum 7: 0.1668
```
*(Output varies slightly)*

## Explanation
- **Simulation**: Rolls two dice `trials` times, counting when their sum equals `target_sum`.
- **Probability**: Estimated as the fraction of successful trials.
- **Complexity**: O(trials) time.
- **Use Case**: Used in education, gaming, or statistical modeling.
- **Best Practice**: Increase `trials` for accuracy; use theoretical calculations for exact probabilities.