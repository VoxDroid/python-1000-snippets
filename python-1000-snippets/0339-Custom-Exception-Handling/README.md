# Custom Exception Handling

## Description
This snippet demonstrates custom exception handling for input validation.

## Code
```python
class InvalidInputError(Exception):
    pass

def check_positive(x):
    if x <= 0:
        raise InvalidInputError("Input must be positive")
    return x

try:
    print("Result:", check_positive(5))
except InvalidInputError as e:
    print("Error:", str(e))
```

## Output
```
Result: 5
```

## Explanation
- **Custom Exception Handling**: Defines and uses a custom exception for validation.
- **Logic**: Raises `InvalidInputError` if input is non-positive.
- **Complexity**: O(1) per check.
- **Use Case**: Used for robust error handling in applications.
- **Best Practice**: Use specific exceptions; provide clear messages; log errors.