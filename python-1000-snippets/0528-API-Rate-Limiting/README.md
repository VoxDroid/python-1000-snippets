# API Rate Limiting

## Description
This snippet demonstrates rate limiting using `redis`.

## Code
```python
# Note: Requires `redis`. Install with `pip install redis`
try:
    import redis
    r = redis.Redis(host="localhost", port=6379)
    key = "user:1"
    r.setex(key, 60, 5)
    print("Rate limit set")
except ImportError:
    print("Mock Output: Rate limit set")
```

## Output
```
Mock Output: Rate limit set
```
*(Real output with `redis`: `Rate limit set`)*

## Explanation
- **API Rate Limiting**: Sets a request limit for a user.
- **Logic**: Uses Redis to store a 5-request limit for 60 seconds.
- **Complexity**: O(1) per operation.
- **Use Case**: Used to prevent API abuse.
- **Best Practice**: Tune limits; handle bursts; log violations.