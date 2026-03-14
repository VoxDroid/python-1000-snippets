# sample1.py
# Create keyspace/table and insert/query a row
from cassandra.cluster import Cluster, NoHostAvailable

if __name__ == '__main__':
    try:
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect()
        session.execute(
            """
            CREATE KEYSPACE IF NOT EXISTS python_snippets
            WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
            """
        )
        session.set_keyspace('python_snippets')
        session.execute(
            "CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY, name text)"
        )
        session.execute(
            "INSERT INTO users (id, name) VALUES (%s, %s)", (1, 'Bob')
        )
        row = session.execute("SELECT name FROM users WHERE id=%s", (1,)).one()
        print('Found:', row.name if row else None)
    except NoHostAvailable as e:
        print('Cassandra not available:', e)
    finally:
        try:
            cluster.shutdown()
        except Exception:
            pass

