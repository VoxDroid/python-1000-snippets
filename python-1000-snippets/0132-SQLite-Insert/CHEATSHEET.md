# 0132-SQLite-Insert Cheatsheet

- **Purpose**: add one or more rows into a table using `INSERT` SQL.
- **Single insert**: `cursor.execute('INSERT INTO tbl(col) VALUES (?)', (val,))`.
- **Batch insert**: use `cursor.executemany(sql, seq_of_params)` for speed.
- **Commit** after inserts to persist results (or use `with` context manager).

```python
import sqlite3
with sqlite3.connect(':memory:') as conn:
    c = conn.cursor()
    c.execute('CREATE TABLE t(x)')
    c.executemany('INSERT INTO t(x) VALUES (?)', [(1,), (2,), (3,)])
    print(c.execute('SELECT COUNT(*) FROM t').fetchone())
```

- Helpful for populating test data or seeds.
- Watch out for SQL injection; always use parameters.

