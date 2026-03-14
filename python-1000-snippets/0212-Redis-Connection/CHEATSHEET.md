# 0212-Redis-Connection Cheatsheet

* Install Python client: `pip install redis`.
* Start Redis server: `redis-server` (default port 6379).
* Connect: `r = redis.Redis(host='localhost', port=6379, db=0)`.
* Basic operations: `r.set('key','value')`, `r.get('key')`, `r.delete('key')`.
* Use `r.mget(['k1','k2'])` for multi-get.
* Hashes: `r.hset('hash', 'field', 'value')`, `r.hgetall('hash')`.
* Lists: `r.lpush('list', 'a')`, `r.rpop('list')`.
* Pub/Sub: `pubsub = r.pubsub(); pubsub.subscribe('channel')` and `pubsub.get_message()`.
* Use `decode_responses=True` to return Python strings instead of bytes.
* Handle connection errors: catch `redis.ConnectionError` and `redis.TimeoutError`.
* For production, use connection pooling (`redis.ConnectionPool`) and configure timeouts.
* Use `r.pipeline()` to batch multiple commands.

