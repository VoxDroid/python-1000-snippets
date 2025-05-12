# Redis PubSub Messaging

## Description
This snippet demonstrates Redis publish/subscribe using `redis`.

## Code
```python
# Note: Requires `redis`. Install with `pip install redis`
try:
    import redis
    r = redis.Redis(host="localhost", port=6379)
    r.publish("channel", "Message")
    print("Message published")
except ImportError:
    print("Mock Output: Message published")
```

## Output
```
Mock Output: Message published
```
*(Real output with `redis` and Redis: Publishes to channel)*

## Explanation
- **Redis PubSub Messaging**: Publishes messages to a Redis channel.
- **Logic**: Connects to Redis and publishes a message.
- **Complexity**: O(1) per publish.
- **Use Case**: Used for real-time messaging or notifications.
- **Best Practice**: Handle connection errors; manage subscriptions; test pub/sub.