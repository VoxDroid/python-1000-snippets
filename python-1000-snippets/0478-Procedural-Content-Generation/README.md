# Procedural Content Generation

## Description
This snippet demonstrates generating a random map using `numpy`.

## Code
```python
try:
    import numpy as np
    map_size = 5
    game_map = np.random.choice([0, 1], size=(map_size, map_size))
    print("Map:\n", game_map)
except ImportError:
    print("""Mock Output: Map:
 [[1 1 0 1 1]
 [1 0 0 0 1]
 [1 1 1 0 1]
 [1 1 0 0 1]
 [0 0 1 1 0]]""")
```

## Output
```
Mock Output: Map: Map:
 [[1 1 0 1 1]
 [1 0 0 0 1]
 [1 1 1 0 1]
 [1 1 0 0 1]
 [0 0 1 1 0]]
```
*(Real output with `numpy`: `Map: <5x5 binary array>`)*

## Explanation
- **Procedural Content Generation**: Creates a random binary map.
- **Logic**: Generates a 5x5 grid with 0s and 1s.
- **Complexity**: O(n) for n cells.
- **Use Case**: Used in games for level generation.
- **Best Practice**: Add patterns; ensure playability; seed for reproducibility.