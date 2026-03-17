# Backtracking

## Description
This snippet demonstrates backtracking algorithms: recursively build candidates and abandon partial solutions that cannot lead to a valid solution.

## Files
- `SAMPLES/sample1.py`: Generate all permutations of a list.
- `SAMPLES/sample2.py`: Solve the N-Queens problem.
- `SAMPLES/sample3.py`: Solve subset sum with backtracking.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Expected output (example)
```
Permutations: [[1, 2, 3], [1, 3, 2], ...]
Solutions for 4-Queens: 2
Subset sum for target 9: True
```

## Explanation
- **Backtracking**: Build solutions incrementally and backtrack when a partial solution can't be extended.
- **Use Case**: Useful for constraint satisfaction, puzzles, and combinatorial search.
- **Best Practice**: Prune early and avoid redundant work when possible.
