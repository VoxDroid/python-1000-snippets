# sample1.py
# simple connect and select example (mocked)

try:
    import psycopg2
    conn = psycopg2.connect(host='localhost', database='test_db', user='user', password='password')
    cur = conn.cursor()
    cur.execute('SELECT 1')
    print('Result:', cur.fetchone())
    conn.close()
except ImportError:
    print("Mock Output: PostgreSQL connection established")
