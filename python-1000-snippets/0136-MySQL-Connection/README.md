# MySQL Connection

## Description
This snippet demonstrates connecting to a MySQL database and executing a simple query. Since this is a demo, it uses a mock setup to avoid real database dependencies.

## Code
```python
# Note: Requires `mysql-connector-python`. Install with `pip install mysql-connector-python`
# This is a mock example; replace with actual credentials for real use
try:
    import mysql.connector
    conn = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="test_db"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test (id INT PRIMARY KEY, name VARCHAR(50))")
    cursor.execute("INSERT INTO test (id, name) VALUES (%s, %s)", (1, "Test"))
    conn.commit()
    cursor.execute("SELECT * FROM test")
    print("Test Data:", cursor.fetchall())
    conn.close()
except ImportError:
    print("Mock Output: MySQL connection established, table created, data inserted: [(1, 'Test')]")
```

## Output
```
Mock Output: MySQL connection established, table created, data inserted: [(1, 'Test')]
```
*(Real output with MySQL: `Test Data: [(1, 'Test')]`)*

## Explanation
- **MySQL Connection**: Uses `mysql-connector-python` to connect to a MySQL database (mocked here).
- **Operations**: Creates a table, inserts data, and queries it.
- **Complexity**: O(1) for connection; O(n) for queries.
- **Use Case**: Used in applications requiring robust relational databases.
- **Best Practice**: Secure credentials; handle connection errors; use environment variables.