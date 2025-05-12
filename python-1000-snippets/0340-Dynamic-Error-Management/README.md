# Dynamic Error Management

## Description
This snippet demonstrates dynamic error management with context-specific handling.

## Code
```python
def process_data(data):
    errors = []
    try:
        result = 10 / data
    except ZeroDivisionError:
        errors.append("Division by zero")
        result = 0
    return result, errors

print("Result, Errors:", process_data(2))
```

## Output
```
Result, Errors: (5.0, [])
```

## Explanation
- **Dynamic Error Management**: Handles errors and collects them for reporting.
- **Logic**: Attempts division, catches errors, and returns result with error list.
- **Complexity**: O(1) per operation.
- **Use Case**: Used in data pipelines or user input processing.
- **Best Practice**: Log errors; handle multiple error types; validate inputs early.