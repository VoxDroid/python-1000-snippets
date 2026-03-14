# sample1.py
# Create a node and query it using Neo4j Python driver
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

if __name__ == '__main__':
    uri = 'bolt://localhost:7687'
    auth = ('neo4j', 'password')

    try:
        driver = GraphDatabase.driver(uri, auth=auth)
        with driver.session() as session:
            session.run("CREATE (p:Person {name: $name})", name='Alice')
            result = session.run("MATCH (p:Person {name: $name}) RETURN p.name AS name", name='Alice')
            record = result.single()
            print('Found:', record['name'] if record else None)
    except ServiceUnavailable as e:
        print('Neo4j not available:', e)
    finally:
        try:
            driver.close()
        except Exception:
            pass

