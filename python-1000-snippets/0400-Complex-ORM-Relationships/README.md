# Complex ORM Relationships

## Description
Demonstrates SQLAlchemy ORM relationships (one-to-many, many-to-many, and eager loading) using an in-memory SQLite database.

## Files
- `SAMPLES/sample1.py` — One-to-many relationship (Parent → Children).
- `SAMPLES/sample2.py` — Many-to-many relationship (Students ↔ Courses).
- `SAMPLES/sample3.py` — Eager loading (joinedload) to reduce query count.

## Usage
Run each sample directly:
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Scripts install `sqlalchemy` at runtime if it's missing.
- Uses SQLite in-memory database, so no external service is required.
