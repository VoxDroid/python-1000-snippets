# PostgreSQL Connection

## Description
This snippet demonstrates connecting to a PostgreSQL database and executing a query. It uses a mock setup to avoid real database dependencies.

## Code
```python
# Note: Requires `psycopg2`. Install with `pip install psycopg2`
# This is a mock example; replace with actual credentials for real use
try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="test_db",
        user="user",
        password="password"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name VARCHAR)")
    cursor.execute("INSERT INTO test (name) VALUES (%s) RETURNING id", ("Test",))
    conn.commit()
    cursor.execute("SELECT * FROM test")
    print("Test Data:", cursor.fetchall())
    conn.close()
except ImportError:
    print("Mock Output: PostgreSQL connection established, table created, data inserted: [(1, 'Test')]")
```

## Output
```
Mock Output: PostgreSQL connection established, table created, data inserted: [(1, 'Test')]
```
*(Real output with PostgreSQL: `Test Data: [(1, 'Test')]`)*

## Explanation
- **PostgreSQL Connection**: Uses `psycopg2` to connect to a PostgreSQL database (mocked here).
- **Operations**: Creates a table, inserts data, and queries it.
- **Complexity**: O(1) for connection; O(n) for queries.
- **Use Case**: Used in scalable applications or enterprise systems.
- **Best Practice**: Secure credentials; use connection pooling for performance.