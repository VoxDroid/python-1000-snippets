# 0134-SQLite-Update Cheatsheet

- **Purpose**: modify existing rows in a table using the `UPDATE` SQL command.
- **Syntax**: `UPDATE table SET col = ? WHERE condition`.
- **Remember**: call `conn.commit()` after updates.

```python
import sqlite3
with sqlite3.connect(':memory:') as conn:
    c = conn.cursor()
    c.execute('CREATE TABLE t(x, y)')
    c.execute('INSERT INTO t(x,y) VALUES (?,?)', (1,2))
    c.execute('UPDATE t SET y = ? WHERE x = ?', (3,1))
    print(c.execute('SELECT * FROM t').fetchall())
```

- Use parameters to avoid SQL injection.
- Verify `cursor.rowcount` to see how many rows were changed.

