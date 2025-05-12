# Persistent Shelve Storage

## Description
This snippet demonstrates persistent storage using `shelve`.

## Code
```python
import shelve

try:
    with shelve.open("data") as db:
        db["key"] = "value"
        print("Stored:", db["key"])
except FileNotFoundError:
    print("Mock Output: Stored: value")
```

## Output
```
Mock Output: Stored: value
```
*(Real output with `shelve`: `Stored: value`)*

## Explanation
- **Persistent Shelve Storage**: Stores key-value pairs persistently.
- **Logic**: Uses `shelve` to store and retrieve data from a file.
- **Complexity**: O(1) per operation (disk-dependent).
- **Use Case**: Used for simple persistent storage or caching.
- **Best Practice**: Handle file access errors; close shelves; use writeback cautiously.