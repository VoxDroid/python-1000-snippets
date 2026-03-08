# 0131-SQLite-Table-Creation Cheatsheet

- **Purpose**: define tables in SQLite using SQL `CREATE TABLE` statements.
- **Syntax**: `CREATE TABLE name (column1 TYPE, column2 TYPE, ...)`.
- **Check existing**: query `sqlite_master` to list tables.
- **Use with Python**:
  ```python
  import sqlite3
  with sqlite3.connect(':memory:') as conn:
      c = conn.cursor()
      c.execute('CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT)')
      c.execute("SELECT name FROM sqlite_master WHERE type='table'")
      print(c.fetchall())
  ```
- **Tips**: include `IF NOT EXISTS` to avoid errors; commit or use context manager.

