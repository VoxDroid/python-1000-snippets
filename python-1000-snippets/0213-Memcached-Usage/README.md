# Memcached Usage

## Description
This snippet demonstrates using Memcached to store and retrieve data using `pylibmc`.

## Code
```python
# Note: Requires `pylibmc`. Install with `pip install pylibmc`
try:
    import pylibmc
    client = pylibmc.Client(["127.0.0.1:11211"])
    client.set("key", "value")
    value = client.get("key")
    print("Value:", value)
except ImportError:
    print("Mock Output: Value: value")
except Exception as e:
    print(f"Error: {e}")
```

## Output
```
Mock Output: Value: value
```
*(Real output with Memcached running: `Value: value`)*

## Explanation
- **Memcached Usage**: Connects to a Memcached server and performs set/get operations.
- **Logic**: Stores a key-value pair using `set` and retrieves it using `get`.
- **Fix for Error**: Removed `.decode()` since `pylibmc.Client.get` returns a string in Python 3, not bytes. If the key is not found, `get` returns `None`, so ensure the key exists or handle `None` cases.
- **Complexity**: O(1) for set/get operations.
- **Use Case**: Used for distributed caching in high-performance applications.
- **Best Practice**: Handle connection timeouts; use consistent hashing; ensure Memcached is running; check for `None` when retrieving values.