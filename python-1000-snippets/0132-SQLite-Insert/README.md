# SQLite Insert

## Description
This snippet inserts records into an SQLite table and retrieves them to verify.

## Code
```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)")
cursor.executemany(
    "INSERT INTO employees (name, salary) VALUES (?, ?)",
    [("Alice", 50000), ("Bob", 60000)]
)
conn.commit()
cursor.execute("SELECT * FROM employees")
print("Employees:", cursor.fetchall())
conn.close()
```

## Output
```
Employees: [(1, 'Alice', 50000.0), (2, 'Bob', 60000.0)]
```

## Explanation
- **SQLite Insert**: Uses `executemany` to insert multiple records with parameterized queries for safety.
- **Table**: Assumes an `employees` table exists; created for demonstration.
- **Complexity**: O(n) for n insertions.
- **Use Case**: Used for adding data to databases in applications.
- **Best Practice**: Commit changes; use parameterized queries to prevent SQL injection.