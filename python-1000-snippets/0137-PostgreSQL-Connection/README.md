# PostgreSQL Connection

## Description
This snippet demonstrates connecting to a PostgreSQL database using `psycopg2` and executing a query. It requires a running PostgreSQL server and valid credentials.

## Code
```python
# Note: Requires `psycopg2`. Install with `pip install psycopg2-binary`
import psycopg2
from psycopg2 import OperationalError

try:
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
except OperationalError as e:
    print("PostgreSQL Error:", e)
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