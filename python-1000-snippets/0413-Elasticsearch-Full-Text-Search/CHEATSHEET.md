# 0413-Elasticsearch-Full-Text-Search Cheatsheet

## Quick start
1. Install Python client:
   ```bash
   pip install elasticsearch
   ```
2. Run a sample:
   ```bash
   python SAMPLES/sample1.py
   ```

## Key concepts
- **Index**: stores documents (like a database table).
- **Document**: a JSON object stored in an index.
- **Full-text search**: use `match` or `multi_match` queries for natural-language text.

## Common operations
- Create an index: `es.indices.create(index="my-index")`
- Index a document: `es.index(index="my-index", id=1, document={...})`
- Search: `es.search(index="my-index", query={"match": {...}})`

## Notes
- The sample scripts start a local Elasticsearch node for testing and stop it when done.
- Use `es.indices.refresh(index=...)` after indexing to make documents searchable immediately.

