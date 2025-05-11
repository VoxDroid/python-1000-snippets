# Finite Element Analysis

## Description
This snippet demonstrates a simple 1D FEA using `numpy` for a bar under tension.

## Code
```python
import numpy as np
K = np.array([[2, -1], [-1, 1]])  # Stiffness matrix
F = np.array([0, 10])  # Force vector
U = np.linalg.solve(K, F)  # Displacement
print("Displacements:", U)
```

## Output
```
Displacements: [10. 20.]
```

## Explanation
- **Finite Element Analysis**: Solves for displacements in a 1D bar.
- **Logic**: Uses a stiffness matrix to compute displacements under force.
- **Complexity**: O(n^3) for n nodes (matrix inversion).
- **Use Case**: Used for structural analysis in engineering.
- **Best Practice**: Validate mesh; use sparse solvers; handle boundary conditions.