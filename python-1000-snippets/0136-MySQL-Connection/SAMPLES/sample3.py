# sample3.py
# insert and fetch a row with parameterized query

try:
    import mysql.connector
    conn = mysql.connector.connect(host='localhost', user='user', password='password', database='test_db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS sample2 (id INT PRIMARY KEY, name VARCHAR(20))')
    cur.execute('INSERT INTO sample2 (id, name) VALUES (%s, %s)', (1, 'Test'))
    conn.commit()
    cur.execute('SELECT * FROM sample2')
    print(cur.fetchall())
    conn.close()
except ImportError:
    print("Mock Output: inserted and fetched [(1, 'Test')]")
