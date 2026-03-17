# Nested List Comprehension

## Description
This snippet demonstrates how to use nested list comprehensions to build and transform 2D data structures (matrices, tables, grids) in a concise and readable way.

## Files
- `SAMPLES/sample1.py`: Create a 2D matrix and compute its transpose.
- `SAMPLES/sample2.py`: Generate a multiplication table using nested comprehensions.
- `SAMPLES/sample3.py`: Parse and filter a CSV-style grid using nested comprehensions.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Matrix: [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
Transpose: [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]]
Multiplication table (5x5): [[1, 2, 3, 4, 5], ...]
Filtered grid: [['A', 'B'], ['E', 'F']]
```

## Explanation
- **Nested list comprehension**: Uses an inner loop inside an outer list expression.
- **Use case**: Generating grids, tables, and applying transformations row-by-row.
- **Best practice**: Keep nesting to 2 levels for readability; consider helper functions if deeper nesting is needed.
