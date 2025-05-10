# Random Walk

## Description
This snippet simulates a 1D random walk, where a particle moves left or right randomly, tracking its position.

## Code
```python
import random

def random_walk(steps):
    position = 0
    positions = [position]
    for _ in range(steps):
        position += random.choice([-1, 1])
        positions.append(position)
    return positions

steps = 10
print("Random Walk:", random_walk(steps))
```

## Output
```
Random Walk: [0, 1, 0, -1, 0, 1, 2, 1, 0, -1, -2]
```
*(Output varies each run)*

## Explanation
- **Random Walk**: Moves +1 or -1 randomly each step, tracking the position.
- **Complexity**: O(steps) time.
- **Use Case**: Used in modeling stock prices, particle diffusion, or statistical physics.
- **Best Practice**: Extend to 2D/3D walks; analyze statistics like mean displacement.