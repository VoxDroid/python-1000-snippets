# 0136-MySQL-Connection Cheatsheet

- **Purpose**: demonstrate connecting to MySQL using `mysql-connector-python` (or mock when unavailable).
- **Installation**: `pip install mysql-connector-python`.
- **Connection**: `conn = mysql.connector.connect(host=..., user=..., password=..., database=...)`.
- **Cursor**: execute SQL with `cursor.execute(sql, params)`; use `%s` placeholders.
- **Cleanup**: call `conn.close()`; or use `with mysql.connector.connect(...) as conn:` if available.
- **Mocking**: the snippet prints a mock message if import fails, useful for testing without MySQL server.

```python
try:
    import mysql.connector
    conn = mysql.connector.connect(host='localhost', user='u', password='p', database='db')
    c = conn.cursor()
    c.execute('SELECT 1')
    print(c.fetchone())
    conn.close()
except ImportError:
    print('Mock MySQL connection')
```

- Use environment variables or config files for credentials in real apps.
- Handle `mysql.connector.Error` for runtime issues.

