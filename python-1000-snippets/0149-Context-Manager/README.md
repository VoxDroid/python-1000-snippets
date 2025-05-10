# Context Manager

## Description
This snippet defines a custom context manager to handle resource setup and cleanup.

## Code
```python
class ResourceManager:
    def __enter__(self):
        print("Resource acquired")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource released")

with ResourceManager() as rm:
    print("Using resource")
```

## Output
```
Resource acquired
Using resource
Resource released
```

## Explanation
- **Context Manager**: Defines `__enter__` (setup) and `__exit__` (cleanup) for resource management.
- **Logic**: Prints messages to show resource lifecycle.
- **Complexity**: O(1) for context operations.
- **Use Case**: Used for file handling, database connections, or locks.
- **Best Practice**: Handle exceptions in `__exit__`; ensure cleanup is idempotent.