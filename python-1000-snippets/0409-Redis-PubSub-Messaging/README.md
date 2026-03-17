# Redis PubSub Messaging

## Description
Demonstrates publish/subscribe messaging using Redis. If a real Redis server is not available, it falls back to `fakeredis` for a pure-Python in-memory simulation.

## Files
- `SAMPLES/sample1.py` — Publish a message and consume it from a subscribed channel.
- `SAMPLES/sample2.py` — (placeholder) could show multiple subscribers.
- `SAMPLES/sample3.py` — (placeholder) could show pattern-based subscriptions.

## Usage
```bash
python SAMPLES/sample1.py
```

## Notes
- Script installs `redis` and `fakeredis` if missing.
- If a Redis server is running on localhost:6379, it will use it; otherwise it uses `fakeredis`.
