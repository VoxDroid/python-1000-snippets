# Return Statement

## Description
This snippet demonstrates the `return` statement in Python, which allows a function to send a value back to the caller for further use.

## Code
```python
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)
```

## Output
```
Sum: 8
```

## Explanation
- **Return Statement**: The `return` keyword exits the function and sends a value (here, `a + b`) back to the caller.
- **Function**: `add(a, b)` takes two parameters, computes their sum, and returns it.
- **Storing Result**: The returned value is stored in `result` for further use or printing.
- **Use Case**: `return` is essential for functions that produce results needed elsewhere, like calculations or data processing.
- **Best Practice**: Ensure functions return meaningful values and avoid side effects (e.g., printing) unless necessary.