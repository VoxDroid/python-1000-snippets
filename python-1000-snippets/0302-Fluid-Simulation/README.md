# Fluid Simulation

## Description
This snippet demonstrates a simplified fluid simulation using a grid-based approach.

## Code
```python
import numpy as np

grid = np.zeros((5, 5))
grid[2, 2] = 1.0  # Initial density in center
new_grid = grid.copy()

for i in range(1, 4):
    for j in range(1, 4):
        # Skip center, and spread its value to neighbors
        if grid[i, j] > 0:
            spread = grid[i, j] * 0.25  # equally spread to 4 neighbors
            new_grid[i-1, j] += spread
            new_grid[i+1, j] += spread
            new_grid[i, j-1] += spread
            new_grid[i, j+1] += spread
            new_grid[i, j] -= spread * 4  # loss from current cell

print("Updated Grid:\n", new_grid)
```

## Output
```
Updated Grid:
 [[0.   0.   0.   0.   0.  ]
 [0.   0.   0.25 0.   0.  ]
 [0.   0.25 0.   0.25 0.  ]
 [0.   0.   0.25 0.   0.  ]
 [0.   0.   0.   0.   0.  ]]
```

## Explanation
- **Fluid Simulation**: Simulates diffusion of a scalar field (density).
- **Logic**: Applies a simple averaging filter to diffuse density.
- **Complexity**: O(r*c) for r rows, c columns.
- **Use Case**: Used for fluid effects in games or animations.
- **Best Practice**: Add velocity fields; use Navier-Stokes; optimize grid size.