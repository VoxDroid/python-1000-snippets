# Constraint Satisfaction

## Description
This snippet demonstrates constraint satisfaction problems (CSPs), where solutions must satisfy a set of constraints.

## Files
- `SAMPLES/sample1.py`: Map coloring (Australia) with 3 colors.
- `SAMPLES/sample2.py`: Solve a 4x4 Sudoku via backtracking and constraints.
- `SAMPLES/sample3.py`: Solve the SEND + MORE = MONEY alphametic puzzle.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Expected output (example)
```
Map coloring:
{'WA': 'Red', 'NT': 'Green', ...}
Sudoku solved:
[[1, 2, 3, 4], ...]
SEND + MORE = MONEY solution: 9567 + 1085 = 10652
```

## Explanation
- **CSP**: Variables have domains and must satisfy constraints.
- **Solving**: Use backtracking and constraint checking (e.g., all-different, adjacency).
- **Use Case**: Scheduling, puzzle solving, and combinatorial design.
