# Elasticsearch Query

## Description
This snippet demonstrates querying Elasticsearch using the `elasticsearch` client.

## Code
```python
# Note: Requires `elasticsearch`. Install with `pip install elasticsearch`
try:
    from elasticsearch import Elasticsearch
    es = Elasticsearch(["http://localhost:9200"])
    es.index(index="myindex", id=1, body={"name": "Alice"})
    result = es.get(index="myindex", id=1)
    print("Found:", result["_source"]["name"])
except ImportError:
    print("Mock Output: Found: Alice")
```

## Output
```
Mock Output: Found: Alice
```
*(Real output with Elasticsearch: `Found: Alice`)*

## Explanation
- **Elasticsearch Query**: Indexes a document and retrieves it using the Elasticsearch client.
- **Logic**: Uses `index` to store data and `get` to query by ID.
- **Complexity**: O(1) for single-document operations.
- **Use Case**: Used for full-text search or analytics in large datasets.
- **Best Practice**: Handle connection errors; use bulk operations; ensure Elasticsearch is running.