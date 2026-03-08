# sample1.py
# select rows satisfying a WHERE clause

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE emp (id INTEGER PRIMARY KEY, salary REAL)')
    c.executemany('INSERT INTO emp (salary) VALUES (?)', [(50000,), (60000,), (45000,)])
    conn.commit()
    c.execute('SELECT id FROM emp WHERE salary > ?', (50000,))
    print('High earners:', c.fetchall())
    conn.close()

if __name__ == '__main__':
    run()
