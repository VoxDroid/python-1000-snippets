# Conjugate Gradient

## Description
This snippet implements the Conjugate Gradient (CG) method for solving symmetric positive-definite linear systems, and for minimizing quadratic functions.

## Files
- `SAMPLES/sample1.py`: Solve Ax = b for a small SPD matrix.
- `SAMPLES/sample2.py`: Solve a larger random SPD system.
- `SAMPLES/sample3.py`: Minimize a quadratic function via CG (equivalent to solving Ax=b).

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Solution: [0.09090909 0.63636364]
Solution: [0.23 0.67 0.11 0.42]
Minimum x: [0.50 0.50], f(x)=0.25
```

## Explanation
- **Conjugate Gradient**: Finds the exact solution in at most n iterations for an n×n SPD matrix.
- **Logic**: Uses conjugate search directions to accelerate convergence.
- **Use Case**: Large sparse linear systems and quadratic minimization.
