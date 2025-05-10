# SQLite Connection

## Description
This snippet demonstrates connecting to an in-memory SQLite database, creating a table, and inserting data.

## Code
```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
cursor.execute("SELECT * FROM users")
print("Users:", cursor.fetchall())
conn.close()
```

## Output
```
Users: [(1, 'Alice')]
```

## Explanation
- **SQLite Connection**: Connects to an in-memory database with `sqlite3.connect`.
- **Operations**: Creates a `users` table, inserts a record, and queries it.
- **Complexity**: O(1) for simple queries.
- **Use Case**: Used for lightweight database applications or prototyping.
- **Best Practice**: Use parameterized queries; handle connection errors.