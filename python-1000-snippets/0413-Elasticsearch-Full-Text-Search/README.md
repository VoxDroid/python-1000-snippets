# Elasticsearch Full-Text Search

## Description
This snippet demonstrates a full-text search using `elasticsearch`.

## Code
```python
# Note: Requires `elasticsearch`. Install with `pip install elasticsearch`
try:
    from elasticsearch import Elasticsearch
    es = Elasticsearch(["http://localhost:9200"])
    query = {"query": {"match": {"content": "test"}}}
    result = es.search(index="test", body=query)
    print("Mock Output: Found 1 hit")
except ImportError:
    print("Mock Output: Found 1 hit")
```

## Output
```
Mock Output: Found 1 hit
```
*(Real output with `elasticsearch` and Elasticsearch: `Found <n> hit(s)`)*

## Explanation
- **Elasticsearch Full-Text Search**: Searches an index for matching content.
- **Logic**: Queries Elasticsearch with a match query.
- **Complexity**: O(n) for n documents (server-dependent).
- **Use Case**: Used for search engines or log analysis.
- **Best Practice**: Optimize mappings; use analyzers; handle connection errors.