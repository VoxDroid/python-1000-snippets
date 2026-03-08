# 0137-PostgreSQL-Connection Cheatsheet

- **Purpose**: show how to connect to PostgreSQL with `psycopg2` (or mock if not installed).
- **Installation**: `pip install psycopg2-binary` for convenience.
- **Connection**:
  ```python
  conn = psycopg2.connect(host='localhost', database='db', user='u', password='p')
  ```
- **Cursor**: use `cur = conn.cursor(); cur.execute(sql, params)` with `%s` placeholders.
- **Cleanup**: `conn.close()`; use context manager `with psycopg2.connect(...) as conn:`.
- **Mock**: the snippet uses a try/except to print a fake result when library missing.

- Real code should handle `psycopg2.Error` and use connection pooling for high load.

