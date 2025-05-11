# Path Planning

## Description
This snippet demonstrates simple path planning using a grid-based approach.

## Code
```python
import numpy as np
grid = np.zeros((5, 5))
grid[2, 2] = 1  # Obstacle
start, goal = (0, 0), (4, 4)
path = [start]
current = start
while current != goal:
    x, y = current
    if x < 4 and grid[x+1, y] == 0:
        current = (x+1, y)
    elif y < 4 and grid[x, y+1] == 0:
        current = (x, y+1)
    else:
        break
    path.append(current)
print("Path:", path)
```

## Output
```
Path: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
```

## Explanation
- **Path Planning**: Finds a path from start to goal avoiding obstacles.
- **Logic**: Uses a greedy approach to move right or down.
- **Complexity**: O(r*c) for r rows, c columns.
- **Use Case**: Used for robot navigation or game AI.
- **Best Practice**: Use A* for optimality; handle complex grids; validate paths.