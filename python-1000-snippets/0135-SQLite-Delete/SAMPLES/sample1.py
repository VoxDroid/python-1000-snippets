# sample1.py
# delete employees with low salary

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE emp (id INTEGER PRIMARY KEY, salary REAL)')
    c.executemany('INSERT INTO emp (salary) VALUES (?)', [(50000,), (60000,)])
    conn.commit()
    c.execute('DELETE FROM emp WHERE salary < ?', (55000,))
    conn.commit()
    c.execute('SELECT * FROM emp')
    print('Remaining Employees:', c.fetchall())
    conn.close()

if __name__ == '__main__':
    run()
