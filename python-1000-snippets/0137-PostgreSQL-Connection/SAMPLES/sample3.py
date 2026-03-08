# sample3.py
# insert and query a row using parameterized query

try:
    import psycopg2
    conn = psycopg2.connect(host='localhost', database='test_db', user='user', password='password')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS sample2 (id SERIAL PRIMARY KEY, name VARCHAR)')
    cur.execute('INSERT INTO sample2 (name) VALUES (%s) RETURNING id', ('Test',))
    conn.commit()
    cur.execute('SELECT * FROM sample2')
    print(cur.fetchall())
    conn.close()
except ImportError:
    print("Mock Output: inserted and fetched [(1, 'Test')]")
