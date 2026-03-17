# 0334-Nested-List-Comprehension Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Matrix + transpose
python SAMPLES/sample2.py  # Multiplication table
python SAMPLES/sample3.py  # Filter a CSV-like grid
```

## Tips
- Use nested list comprehensions to generate 2D lists:
  `matrix = [[f(i, j) for j in range(cols)] for i in range(rows)]`
- Use `zip(*matrix)` to transpose a matrix.
- Apply filtering inside the inner list comprehension with a conditional.

## Example outline
```python
matrix = [[i * cols + j for j in range(cols)] for i in range(rows)]
transpose = [list(row) for row in zip(*matrix)]
``` 
