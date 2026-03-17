# 0338-Recursive-Functions Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Memoized factorial
python SAMPLES/sample2.py  # Recursive nested dict traversal
python SAMPLES/sample3.py  # Recursive merge sort
```

## Tips
- Always define a base case to stop recursion.
- For expensive recursive computations, use memoization or caching (`functools.lru_cache`).
- Use recursion for tree-like and nested data structures.

## Common patterns
- Factorial:
  ```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
  ```
- Traversal: Recursively visit children and aggregate results.
- Divide and conquer: Split list, recurse, then merge results.
