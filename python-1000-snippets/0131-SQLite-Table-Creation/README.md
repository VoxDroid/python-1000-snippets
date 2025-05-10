# SQLite Table Creation

## Description
This snippet demonstrates creating a table in an in-memory SQLite database using the `sqlite3` module.

## Code
```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        salary REAL
    )
""")
conn.commit()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cursor.fetchall())
conn.close()
```

## Output
```
Tables: [('employees',)]
```

## Explanation
- **SQLite Table Creation**: Uses `CREATE TABLE` to define an `employees` table with `id`, `name`, and `salary` columns.
- **Connection**: Connects to an in-memory database (`:memory:`) for temporary storage.
- **Query**: Verifies table creation by querying `sqlite_master`.
- **Complexity**: O(1) for table creation.
- **Use Case**: Used in lightweight applications or prototyping database schemas.
- **Best Practice**: Use parameterized queries for safety; close connections properly.