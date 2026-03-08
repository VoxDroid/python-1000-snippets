# sample2.py
# create table if possible, else mock output

try:
    import mysql.connector
    conn = mysql.connector.connect(host='localhost', user='user', password='password', database='test_db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS sample (id INT PRIMARY KEY)')
    conn.commit()
    print('Table created (real)')
    conn.close()
except ImportError:
    print('Mock Output: table created')
