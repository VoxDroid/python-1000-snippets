# Redis Connection

## Description
This snippet demonstrates connecting to Redis and performing basic operations using `redis-py`.

## Code
```python
# Note: Requires `redis`. Install with `pip install redis`
try:
    import redis
    r = redis.Redis(host="localhost", port=6379, db=0)
    r.set("key", "value")
    print("Value:", r.get("key").decode())
except ImportError:
    print("Mock Output: Value: value")
```

## Output
```
Mock Output: Value: value
```
*(Real output with Redis: `Value: value`)*

## Explanation
- **Redis Connection**: Connects to a Redis server and performs set/get operations.
- **Logic**: Stores a key-value pair and retrieves it.
- **Complexity**: O(1) for set/get operations.
- **Use Case**: Used for caching, session management, or pub-sub messaging.
- **Best Practice**: Handle connection errors; use connection pooling; ensure Redis is running.