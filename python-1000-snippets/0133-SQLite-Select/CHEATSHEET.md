# 0133-SQLite-Select Cheatsheet

- **Purpose**: retrieve data using `SELECT` queries, optionally filtering with `WHERE`.
- **Basic form**: `cursor.execute('SELECT col1, col2 FROM table WHERE condition', params)`.
- **Fetching**: use `cursor.fetchall()` or `cursor.fetchone()`.
- **Parameterized queries**: always pass parameters as a tuple to avoid injection.

```python
import sqlite3
with sqlite3.connect(':memory:') as conn:
    c = conn.cursor()
    c.execute('CREATE TABLE t(x)')
    c.execute('INSERT INTO t(x) VALUES (?)', (10,))
    c.execute('SELECT x FROM t WHERE x > ?', (5,))
    print(c.fetchall())
```

- For large results, iterate with `for row in c:` to avoid loading all rows.
- Use `ORDER BY` or `LIMIT` to control output.

