# Neo4j Connection

## Description
This snippet demonstrates connecting to Neo4j and creating/querying a node using `neo4j`.

## Code
```python
# Note: Requires `neo4j`. Install with `pip install neo4j`
try:
    from neo4j import GraphDatabase
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
    with driver.session() as session:
        session.run("CREATE (p:Person {name: 'Alice'})")
        result = session.run("MATCH (p:Person {name: 'Alice'}) RETURN p.name")
        print("Found:", result.single()[0])
    driver.close()
except ImportError:
    print("Mock Output: Found: Alice")
```

## Output
```
Mock Output: Found: Alice
```
*(Real output with Neo4j: `Found: Alice`)*

## Explanation
- **Neo4j Connection**: Connects to Neo4j, creates a node, and queries it using Cypher.
- **Logic**: Uses `run` to execute Cypher queries within a session.
- **Complexity**: O(1) for single-node operations.
- **Use Case**: Used for graph-based data like social networks or recommendations.
- **Best Practice**: Manage sessions; secure credentials; ensure Neo4j is running.