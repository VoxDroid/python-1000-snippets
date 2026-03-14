# 0217-Neo4j-Connection Cheatsheet

* Install Python driver: `pip install neo4j`.
* Run Neo4j server and set password for `neo4j` user; default bolt URI is `bolt://localhost:7687`.
* Connect: `driver = GraphDatabase.driver(uri, auth=('neo4j','password'))`.
* Use sessions: `with driver.session() as session:` and `session.run(cypher, **params)`.
* Create nodes: `CREATE (p:Person {name: $name})` with parameterized queries.
* Read data: `MATCH (p:Person) RETURN p.name`.
* Use transactions: `with session.begin_transaction() as tx:`.
* Close driver: `driver.close()`.
* Handle `neo4j.exceptions.ServiceUnavailable` when server is down.
* For bulk imports, use `UNWIND` to insert multiple rows.
* Use labels and indexes for performance: `CREATE INDEX FOR (p:Person) ON (p.name)`.

