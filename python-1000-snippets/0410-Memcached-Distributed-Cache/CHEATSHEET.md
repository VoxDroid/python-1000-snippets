# 0410-Memcached-Distributed-Cache Cheatsheet

## Quick start
1. Ensure you have `memcached` installed and available on `PATH`.
2. Install the Python client library:
   ```bash
   pip install pymemcache
   ```
3. Run an example:
   ```bash
   python SAMPLES/sample1.py
   ```

## Key concepts
- **Client**: `pymemcache.client.base.Client((host, port))`
- **Set**: `client.set("key", "value")`
- **Get**: `client.get("key")`
- **Multi-get**: `client.get_many(["key1", "key2"])`
- **Increment/Decrement**: `client.incr("counter", 1)`, `client.decr("counter", 1)`

## Notes
- The samples start a local `memcached` process and write its output to `./temp/memcached.log`.
- If the script cannot start `memcached`, it will raise an error (so you can install it and rerun).

