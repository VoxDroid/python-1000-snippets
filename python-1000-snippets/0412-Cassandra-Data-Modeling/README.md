# Cassandra Data Modeling

## Description
This snippet demonstrates a Cassandra table creation using `cassandra-driver`.

## Code
```python
# Note: Requires `cassandra-driver`. Install with `pip install cassandra-driver`
try:
    from cassandra.cluster import Cluster
    cluster = Cluster(["localhost"])
    session = cluster.connect("test")
    session.execute("CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY, name text)")
    print("Table created")
except ImportError:
    print("Mock Output: Table created")
```

## Output
```
Mock Output: Table created
```
*(Real output with `cassandra-driver` and Cassandra: `Table created`)*

## Explanation
- **Cassandra Data Modeling**: Creates a table for user data.
- **Logic**: Connects to Cassandra and executes a CQL create table command.
- **Complexity**: O(1) for table creation.
- **Use Case**: Used for scalable, distributed data storage.
- **Best Practice**: Design for query patterns; use appropriate partition keys; test schema.