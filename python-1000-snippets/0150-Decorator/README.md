# Decorator

## Description
This snippet defines a decorator to measure the execution time of a function.

## Code
```python
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper

@timing_decorator
def slow_function(n):
    time.sleep(n)
    return n

print("Result:", slow_function(1))
```

## Output
```
slow_function took 1.00s
Result: 1
```

## Explanation
- **Decorator**: Wraps `slow_function` with `timing_decorator` to measure and print execution time.
- **Logic**: Uses `time.time()` to calculate duration.
- **Complexity**: O(1) overhead plus function runtime.
- **Use Case**: Used for logging, profiling, or authentication.
- **Best Practice**: Preserve function metadata with `functools.wraps`; handle exceptions in decorators.