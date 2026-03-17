# SQLAlchemy Query Optimization

## Description
Demonstrates common query optimization techniques with SQLAlchemy (limit, indexing, eager loading, and select statement building). Uses an in-memory SQLite database.

## Files
- `SAMPLES/sample1.py` — Use `limit()` to avoid fetching too many rows.
- `SAMPLES/sample2.py` — Use `joinedload()` to eager-load relationships.
- `SAMPLES/sample3.py` — Build a `select()` statement with filtering and ordering.

## Usage
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Scripts install `sqlalchemy` if it's missing.
- In-memory SQLite avoids external dependencies.
