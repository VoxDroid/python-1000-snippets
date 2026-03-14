# sample2.py
# Update a node property using a transaction
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

if __name__ == '__main__':
    uri = 'bolt://localhost:7687'
    auth = ('neo4j', 'password')

    try:
        driver = GraphDatabase.driver(uri, auth=auth)
        with driver.session() as session:
            session.run(
                "MATCH (p:Person {name: $old}) SET p.name = $new RETURN p.name",
                old='Alice',
                new='Alice Updated',
            )
            result = session.run("MATCH (p:Person {name: $name}) RETURN p.name AS name", name='Alice Updated')
            print('Updated:', result.single()['name'])
    except ServiceUnavailable as e:
        print('Neo4j not available:', e)
    finally:
        try:
            driver.close()
        except Exception:
            pass

