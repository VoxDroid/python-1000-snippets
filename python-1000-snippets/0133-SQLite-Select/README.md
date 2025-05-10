# SQLite Select

## Description
This snippet retrieves records from an SQLite table using a `SELECT` query with a condition.

## Code
```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)")
cursor.executemany(
    "INSERT INTO employees (name, salary) VALUES (?, ?)",
    [("Alice", 50000), ("Bob", 60000), ("Charlie", 45000)]
)
conn.commit()
cursor.execute("SELECT name, salary FROM employees WHERE salary > ?", (50000,))
print("High Earners:", cursor.fetchall())
conn.close()
```

## Output
```
High Earners: [('Bob', 60000.0)]
```

## Explanation
- **SQLite Select**: Uses `SELECT` with a `WHERE` clause to filter employees with salary > 50000.
- **Parameterized Query**: Prevents SQL injection by using `?` placeholders.
- **Complexity**: O(n) for scanning n rows.
- **Use Case**: Used for querying data in applications or reports.
- **Best Practice**: Index columns for performance; handle empty result sets.