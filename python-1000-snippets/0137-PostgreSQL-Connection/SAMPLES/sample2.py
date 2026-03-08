# sample2.py
# create table (mocked if library unavailable)

try:
    import psycopg2
    conn = psycopg2.connect(host='localhost', database='test_db', user='user', password='password')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS sample (id SERIAL PRIMARY KEY)')
    conn.commit()
    print('Table created (real)')
    conn.close()
except ImportError:
    print('Mock Output: table created')
