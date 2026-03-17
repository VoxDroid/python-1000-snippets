# 0409-Redis-PubSub-Messaging Cheatsheet

- Install `redis` and `fakeredis` with `python -m pip install redis fakeredis`.
- Use `Redis().pubsub()` and `.subscribe(channel)` to listen for messages.
- Use `publish(channel, message)` to send messages.
- `pubsub.get_message(timeout=...)` can poll without blocking indefinitely.
- Fall back to `fakeredis.FakeRedis()` if no Redis server is available.
