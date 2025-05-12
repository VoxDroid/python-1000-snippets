# Terrain Generation

## Description
This snippet demonstrates terrain generation using Perlin noise with `noise`.

## Code
```python
# Note: Requires `noise`. Install with `pip install noise`
try:
    import noise
    import numpy as np
    shape = (5, 5)
    terrain = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            terrain[i][j] = noise.pnoise2(i * 0.1, j * 0.1)
    print("Terrain:\n", terrain)
except ImportError:
    print("Mock Output: Terrain: [[0.1 0.2 ...] ...]")
```

## Output
```
Mock Output: Terrain: [[0.1 0.2 ...] ...]
```
*(Real output with `noise`: `Terrain: <5x5 noise array>`)*

## Explanation
- **Terrain Generation**: Creates a 2D terrain using Perlin noise.
- **Logic**: Generates smooth noise values for a 5x5 grid.
- **Complexity**: O(n) for n cells.
- **Use Case**: Used in games or simulations for realistic terrain.
- **Best Practice**: Tune noise scale; normalize values; visualize terrain.