# Recursive Functions

## Description
This snippet demonstrates recursive function patterns for mathematical computations and traversals.

## Files
- `SAMPLES/sample1.py`: Recursive factorial with memoization.
- `SAMPLES/sample2.py`: Recursive traversal of nested dictionaries.
- `SAMPLES/sample3.py`: Recursive merge sort implementation.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Factorial(10): 3628800
Nested keys: ['a.b.c', 'a.d', 'e']
Sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Explanation
- **Recursive functions**: A function calls itself with modified arguments until a base case is reached.
- **Logic**: Ensure each recursive call progresses toward the base case to avoid infinite recursion.
- **Use Case**: Useful for divide-and-conquer algorithms, traversals, and combinatorial generation.
- **Best Practice**: Use memoization for overlapping subproblems; avoid deep recursion where possible.
