# Recursive Functions

## Description
This snippet demonstrates a recursive function to compute factorials.

## Code
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial(5):", factorial(5))
```

## Output
```
Factorial(5): 120
```

## Explanation
- **Recursive Functions**: Computes n! using recursion.
- **Logic**: Base case returns 1; recursive case multiplies n by (n-1)!.
- **Complexity**: O(n) for n calls.
- **Use Case**: Used for tree traversals or combinatorial problems.
- **Best Practice**: Optimize with memoization; handle stack overflow; validate inputs.