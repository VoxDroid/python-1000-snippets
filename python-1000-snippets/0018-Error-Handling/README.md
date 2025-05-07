# Error Handling

## Description
This snippet demonstrates error handling in Python using `try`, `except`, `else`, and `finally` to manage exceptions gracefully.

## Code
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")
```

## Output
```
Enter a number: 5
Result: 2.0
Execution complete.
```
*(If input is `0`):*
```
Enter a number: 0
Cannot divide by zero.
Execution complete.
```
*(If input is `"abc"`):*
```
Enter a number: abc
Please enter a valid integer.
Execution complete.
```

## Explanation
- **Try-Except**: `try` runs code that might raise an exception; `except` handles specific exceptions (e.g., `ValueError`, `ZeroDivisionError`).
- **Else**: Runs if no exception occurs, useful for code dependent on successful `try`.
- **Finally**: Always executes, regardless of exceptions, for cleanup or final steps.
- **Use Case**: Error handling ensures robust programs, like validating user input or handling file operations.
- **Best Practice**: Catch specific exceptions rather than a generic `except` to avoid masking unexpected errors.