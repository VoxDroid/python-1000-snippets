# Distributed Locking

## Description
This snippet demonstrates distributed locking using `redis`.

## Code
```python
# Note: Requires `redis`. Install with `pip install redis`
try:
    import redis
    r = redis.Redis(host="localhost", port=6379)
    lock = r.lock("resource", timeout=10)
    lock.acquire()
    print("Lock acquired")
    lock.release()
except ImportError:
    print("Mock Output: Lock acquired")
```

## Output
```
Mock Output: Lock acquired
```
*(Real output with `redis`: `Lock acquired`)*

## Explanation
- **Distributed Locking**: Ensures exclusive resource access across systems.
- **Logic**: Acquires and releases a Redis lock.
- **Complexity**: O(1) per lock operation (network-dependent).
- **Use Case**: Used in distributed systems for synchronization.
- **Best Practice**: Set timeouts; handle failures; monitor locks.