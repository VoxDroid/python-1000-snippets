# Thread-Safe Singleton

## Description
This snippet demonstrates a thread-safe singleton pattern.

## Code
```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
```

## Output
```
True
```

## Explanation
- **Thread-Safe Singleton**: Ensures a single instance across threads.
- **Logic**: Uses a lock to prevent concurrent instance creation.
- **Complexity**: O(1) with contention overhead.
- **Use Case**: Used for shared resources like loggers or configurations.
- **Best Practice**: Use locks sparingly; consider module-level singletons; test concurrency.