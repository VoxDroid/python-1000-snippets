# sample1.py
# simple connect-and-query example (mocked)

try:
    import mysql.connector
    conn = mysql.connector.connect(host='localhost', user='user', password='password', database='test_db')
    cur = conn.cursor()
    cur.execute('SELECT 1')
    print('Result:', cur.fetchone())
    conn.close()
except ImportError:
    print("Mock Output: MySQL connection established")
