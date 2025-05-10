# Shelve Usage

## Description
This snippet demonstrates using `shelve` to store and retrieve key-value pairs persistently.

## Code
```python
import shelve

with shelve.open("mystore") as db:
    db["user1"] = {"name": "Alice", "age": 25}
    db["user2"] = {"name": "Bob", "age": 30}

with shelve.open("mystore") as db:
    print("User1:", db["user1"])
    print("User2:", db["user2"])
```

## Output
```
User1: {'name': 'Alice', 'age': 25}
User2: {'name': 'Bob', 'age': 30}
```

## Explanation
- **Shelve Usage**: Uses `shelve` to store dictionaries in a persistent key-value store.
- **Logic**: Saves and retrieves data using dictionary-like access.
- **Complexity**: O(1) for key-value operations.
- **Use Case**: Used for simple persistent storage without a full database.
- **Best Practice**: Use `with` for safe access; avoid large datasets; handle key errors.