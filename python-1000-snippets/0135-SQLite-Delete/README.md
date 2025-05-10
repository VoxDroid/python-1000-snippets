# SQLite Delete

## Description
This snippet deletes records from an SQLite table based on a condition.

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
cursor.execute("DELETE FROM employees WHERE salary < ?", (55000,))
conn.commit()
cursor.execute("SELECT * FROM employees")
print("Remaining Employees:", cursor.fetchall())
conn.close()
```

## Output
```
Remaining Employees: [(2, 'Bob', 60000.0)]
```

## Explanation
- **SQLite Delete**: Uses `DELETE` to remove employees with salary < 55000.
- **Parameterized Query**: Uses `?` for safety.
- **Complexity**: O(n) for scanning n rows.
- **Use Case**: Used for removing obsolete data in applications.
- **Best Practice**: Commit changes; use precise conditions to avoid data loss.