# sample2.py
# Use prepared statement and update data
from cassandra.cluster import Cluster, NoHostAvailable

if __name__ == '__main__':
    try:
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect('python_snippets')
        stmt = session.prepare('UPDATE users SET name = ? WHERE id = ?')
        session.execute(stmt, ('Bob Updated', 1))
        row = session.execute('SELECT name FROM users WHERE id=%s', (1,)).one()
        print('Updated name:', row.name if row else None)
    except NoHostAvailable as e:
        print('Cassandra not available:', e)
    finally:
        try:
            cluster.shutdown()
        except Exception:
            pass

