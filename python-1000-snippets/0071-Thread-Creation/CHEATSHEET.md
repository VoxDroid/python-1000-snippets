# Thread Creation Cheatsheet

## Starting threads
```python
import threading
threading.Thread(target=func, args=(arg,)).start()
```

## Joining
`thread.join()` waits for completion.

## Locks
```
lock = threading.Lock()
with lock:
    # critical section
```

## Daemon threads
`thread.daemon = True` exits when main thread exits.

## Tips
- Use `queue.Queue` for thread-safe data sharing.
- Avoid modifying global state without locks.

## Running samples
Activate venv and run `SAMPLES/sample*.py`.
