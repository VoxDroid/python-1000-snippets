# MongoDB Connection

## Description
This snippet demonstrates connecting to MongoDB and performing a basic insert/query using `pymongo`.

## Code
```python
# Note: Requires `pymongo`. Install with `pip install pymongo`
try:
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydb"]
    collection = db["users"]
    collection.insert_one({"name": "Alice"})
    result = collection.find_one({"name": "Alice"})
    print("Found:", result["name"])
except ImportError:
    print("Mock Output: Found: Alice")
```

## Output
```
Mock Output: Found: Alice
```
*(Real output with MongoDB: `Found: Alice`)*

## Explanation
- **MongoDB Connection**: Connects to MongoDB, inserts a document, and queries it.
- **Logic**: Uses `insert_one` and `find_one` for basic CRUD operations.
- **Complexity**: O(1) for single-document operations.
- **Use Case**: Used for NoSQL data storage in flexible-schema applications.
- **Best Practice**: Handle connection errors; index fields; ensure MongoDB is running.