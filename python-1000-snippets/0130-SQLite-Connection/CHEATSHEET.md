# 0130-SQLite-Connection Cheatsheet

- **Purpose**: open an SQLite database (memory or file) and run simple SQL statements.
- **Connection**: `conn = sqlite3.connect(':memory:')` for ephemeral DB, or a filename for persistent.
- **Cursor**: use `cursor = conn.cursor()` and `cursor.execute(sql, params)`.
- **Parameterization**: always use `?` placeholders to avoid injection.
- **Commit/close**: call `conn.commit()` to save changes and `conn.close()` when done.

```python
import sqlite3
with sqlite3.connect('data.db') as conn:
    c = conn.cursor()
    c.execute('CREATE TABLE t(x)')
    c.execute('INSERT INTO t(x) VALUES (?)', (42,))
    print(c.fetchall())
```

- Useful for prototyping or lightweight persistence.
- Results are Python tuples (e.g., `[(1, 'Alice')]`).

