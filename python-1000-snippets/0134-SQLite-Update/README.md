# SQLite Update

## Description
This snippet updates records in an SQLite table based on a condition.

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
cursor.execute("UPDATE employees SET salary = ? WHERE name = ?", (55000, "Alice"))
conn.commit()
cursor.execute("SELECT * FROM employees")
print("Updated Employees:", cursor.fetchall())
conn.close()
```

## Output
```
Updated Employees: [(1, 'Alice', 55000.0), (2, 'Bob', 60000.0)]
```

## Explanation
- **SQLite Update**: Uses `UPDATE` to modify `salary` for a specific employee.
- **Parameterized Query**: Ensures safety with `?` placeholders.
- **Complexity**: O(n) for scanning n rows to find matches.
- **Use Case**: Used for modifying existing data in applications.
- **Best Practice**: Commit changes; verify update conditions to avoid unintended changes.