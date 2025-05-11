# Cassandra Connection

## Description
This snippet demonstrates connecting to Cassandra and performing a basic insert/query using `cassandra-driver`.

## Code
```python
# Note: Requires `cassandra-driver`. Install with `pip install cassandra-driver`
try:
    from cassandra.cluster import Cluster
    cluster = Cluster(["localhost"])
    session = cluster.connect("mykeyspace")
    session.execute("CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY, name text)")
    session.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (1, "Bob"))
    rows = session.execute("SELECT name FROM users WHERE id = %s", (1,))
    print("Found:", rows.one().name)
except ImportError:
    print("Mock Output: Found: Bob")
```

## Output
```
Mock Output: Found: Bob
```
*(Real output with Cassandra: `Found: Bob`)*

## Explanation
- **Cassandra Connection**: Connects to Cassandra, creates a table, inserts data, and queries it.
- **Logic**: Uses `execute` for CQL statements with parameterized queries.
- **Complexity**: O(1) for single-row operations.
- **Use Case**: Used for distributed, high-availability NoSQL databases.
- **Best Practice**: Use prepared statements; handle cluster failures; ensure Cassandra is running.