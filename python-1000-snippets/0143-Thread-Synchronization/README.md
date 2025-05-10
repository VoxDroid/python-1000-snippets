# Thread Synchronization

## Description
This snippet demonstrates thread synchronization using a lock to safely increment a shared counter.

## Code
```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("Final Counter:", counter)
```

## Output
```
Final Counter: 200000
```

## Explanation
- **Thread Synchronization**: Uses `threading.Lock` to prevent race conditions when updating `counter`.
- **Logic**: Two threads increment `counter` 100,000 times each; lock ensures atomic updates.
- **Complexity**: O(n) for n increments.
- **Use Case**: Used in multi-threaded applications with shared resources.
- **Best Practice**: Minimize lock scope; use `with` for locks; consider `threading.RLock` for recursive locking.