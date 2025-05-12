# Nested Context Managers

## Description
This snippet demonstrates nested context managers for managing multiple resources.

## Code
```python
from contextlib import contextmanager

@contextmanager
def resource(name):
    print(f"Opening {name}")
    yield
    print(f"Closing {name}")

with resource("A"):
    with resource("B"):
        print("Inside nested context")
```

## Output
```
Opening A
Opening B
Inside nested context
Closing B
Closing A
```

## Explanation
- **Nested Context Managers**: Manages multiple resources using nested `with` statements.
- **Logic**: Defines a custom context manager to simulate resource opening/closing.
- **Complexity**: O(1) per context manager.
- **Use Case**: Used for managing multiple files, database connections, or locks.
- **Best Practice**: Use `contextlib` for simplicity; ensure cleanup; handle exceptions.