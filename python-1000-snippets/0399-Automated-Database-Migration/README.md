# Automated Database Migration

## Description
This snippet demonstrates a simple database migration simulation using `sqlalchemy`.

## Code
```python
# Note: Requires `sqlalchemy`. Install with `pip install sqlalchemy`
try:
    from sqlalchemy import create_engine, Table, Column, Integer, MetaData
    engine = create_engine("sqlite:///:memory:")
    metadata = MetaData()
    table = Table("example", metadata, Column("id", Integer, primary_key=True))
    metadata.create_all(engine)
    print("Table created")
except ImportError:
    print("Mock Output: Table created")
```

## Output
```
Mock Output: Table created
```
*(Real output with `sqlalchemy`: `Table created`)*

## Explanation
- **Automated Database Migration**: Creates a database table programmatically.
- **Logic**: Defines a table schema and applies it to an in-memory SQLite database.
- **Complexity**: O(1) for simple schema creation.
- **Use Case**: Used for database setup or migrations.
- **Best Practice**: Use migration tools like Alembic; validate schemas; test migrations.