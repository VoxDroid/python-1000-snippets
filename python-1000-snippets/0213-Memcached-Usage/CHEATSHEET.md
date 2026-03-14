# 0213-Memcached-Usage Cheatsheet

* Install Python client: `pip install pylibmc`.
* Start memcached server: `memcached -p 11211`.
* Connect: `client = pylibmc.Client(['127.0.0.1:11211'])`.
* Set/get cache: `client.set('key', 'value')`, `client.get('key')`.
* Use `client.get_multi(['k1','k2'])` for batch retrieval.
* Keys are typically limited to 250 bytes; values can be binary.
* Set expiration: `client.set('key', 'value', time=10)`.
* Use `client.delete('key')` to evict items.
* Use consistent hashing by passing `binary=True` and `behaviors={'tcp_nodelay': True}`.
* Handle `pylibmc.Error` for connection or server errors.
* Avoid storing large values; memcached is meant for ephemeral caching.

