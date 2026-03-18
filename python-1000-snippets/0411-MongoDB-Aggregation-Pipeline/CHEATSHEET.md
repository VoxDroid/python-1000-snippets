# 0411-MongoDB-Aggregation-Pipeline Cheatsheet

## Quick start
1. Install dependencies:
   ```bash
   pip install pymongo
   ```
2. Run a sample:
   ```bash
   python SAMPLES/sample1.py
   ```

## Key MongoDB aggregation stages
- `$match`: filter documents
- `$group`: group documents and compute aggregates
- `$sort`: order results
- `$project`: reshape documents
- `$limit`: restrict document count

## Tips
- Use `MongoClient(..., serverSelectionTimeoutMS=1000)` to avoid long hangs when the server is unavailable.
- Clear collections between runs with `collection.delete_many({})`.
- Aggregation pipelines are executed on the server; keep stages efficient and indexed.

