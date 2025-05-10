# Monte Carlo Simulation

## Description
This snippet estimates the value of π using a Monte Carlo method by simulating random points in a square and circle.

## Code
```python
import random

def estimate_pi(trials):
    inside_circle = 0
    for _ in range(trials):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return 4 * inside_circle / trials

trials = 100000
print(f"Estimated π: {estimate_pi(trials):.4f}")
```

## Output
```
Estimated π: 3.1416
```
*(Output varies slightly)*

## Explanation
- **Monte Carlo**: Estimates π by comparing the ratio of points inside a unit circle to a 2x2 square; π ≈ 4 * (points in circle / total points).
- **Complexity**: O(trials) time.
- **Use Case**: Used in numerical integration, risk analysis, or physics simulations.
- **Best Practice**: Increase `trials` for accuracy; use parallel processing for large simulations.