# sample3.py
# Delete created nodes and demonstrate cleanup
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

if __name__ == '__main__':
    uri = 'bolt://localhost:7687'
    auth = ('neo4j', 'password')

    try:
        driver = GraphDatabase.driver(uri, auth=auth)
        with driver.session() as session:
            session.run("MATCH (p:Person) WHERE p.name STARTS WITH $prefix DETACH DELETE p", prefix='Alice')
            print('Deleted nodes starting with Alice')
    except ServiceUnavailable as e:
        print('Neo4j not available:', e)
    finally:
        try:
            driver.close()
        except Exception:
            pass

