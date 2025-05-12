# Decorator Stacking

## Description
This snippet demonstrates stacking multiple decorators on a function.

## Code
```python
def log(func):
    def wrapper(*args):
        print(f"Calling {func.__name__}")
        return func(*args)
    return wrapper

def timer(func):
    def wrapper(*args):
        print(f"Timing {func.__name__}")
        return func(*args)
    return wrapper

@log
@timer
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
```

## Output
```
Calling wrapper
Timing greet
Hello, Alice
```

## Explanation
- **Decorator Stacking**: Applies multiple decorators to log and time a function.
- **Logic**: `log` and `timer` decorators wrap the function, executing in order.
- **Complexity**: O(1) per decorator call.
- **Use Case**: Used for logging, timing, or access control in functions.
- **Best Practice**: Ensure decorator order; maintain function metadata; handle arguments.