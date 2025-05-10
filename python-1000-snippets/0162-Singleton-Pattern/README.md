# Singleton Pattern

## Description
This snippet implements the Singleton pattern to ensure only one instance of a class exists.

## Code
```python
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print("Same instance:", s1 is s2)
```

## Output
```
Same instance: True
```

## Explanation
- **Singleton Pattern**: Ensures a single instance by overriding `__new__`.
- **Logic**: Stores the instance in `_instance`; reuses it for all calls.
- **Complexity**: O(1) for instance creation/check.
- **Use Case**: Used for shared resources like loggers or configurations.
- **Best Practice**: Ensure thread-safety if used in multi-threaded environments.