# Memcached Distributed Cache

## Description
This snippet demonstrates caching with `pylibmc`.

## Code
```python
# Note: Requires `pylibmc`. Install with `pip install pylibmc`
try:
    import pylibmc
    client = pylibmc.Client(["127.0.0.1"])
    client.set("key", "value")
    print("Cached:", client.get("key"))
except ImportError:
    print("Mock Output: Cached: value")
```

## Output
```
Mock Output: Cached: value
```
*(Real output with `pylibmc` and Memcached: `Cached: value`)*

## Explanation
- **Memcached Distributed Cache**: Stores and retrieves data in Memcached.
- **Logic**: Connects to Memcached and sets/gets a key-value pair.
- **Complexity**: O(1) per operation.
- **Use Case**: Used for caching database queries or session data.
- **Best Practice**: Handle connection failures; set expiration; monitor cache usage.