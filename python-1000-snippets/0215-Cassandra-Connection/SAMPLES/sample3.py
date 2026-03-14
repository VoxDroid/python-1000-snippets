# sample3.py
# Demonstrate batch insert using BATCH statement
from cassandra.cluster import Cluster, NoHostAvailable

if __name__ == '__main__':
    try:
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect('python_snippets')
        batch = """
        BEGIN BATCH
        INSERT INTO users (id, name) VALUES (2, 'Carol');
        INSERT INTO users (id, name) VALUES (3, 'Dave');
        APPLY BATCH
        """
        session.execute(batch)
        rows = session.execute('SELECT id, name FROM users')
        print('Users:', [(r.id, r.name) for r in rows])
    except NoHostAvailable as e:
        print('Cassandra not available:', e)
    finally:
        try:
            cluster.shutdown()
        except Exception:
            pass

