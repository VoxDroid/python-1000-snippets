# 0135-SQLite-Delete Cheatsheet

- **Purpose**: remove rows from a table using `DELETE FROM` with conditions.
- **Basic syntax**: `DELETE FROM table WHERE condition`.
- **Be careful**: leaving out `WHERE` deletes all rows.
- **Commit** after deletion.

```python
import sqlite3
with sqlite3.connect(':memory:') as conn:
    c = conn.cursor()
    c.execute('CREATE TABLE t(x)')
    c.execute('INSERT INTO t(x) VALUES (?)', (1,))
    c.execute('DELETE FROM t WHERE x = ?', (1,))
    print(c.execute('SELECT * FROM t').fetchall())
```

- `cursor.rowcount` tells how many rows were deleted.
- Use `VACUUM` if deleting many rows to reclaim space.

