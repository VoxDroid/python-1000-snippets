# sample1.py
# update a salary value for one employee

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE emp (id INTEGER PRIMARY KEY, salary REAL)')
    c.execute('INSERT INTO emp (salary) VALUES (?)', (50000,))
    conn.commit()
    c.execute('UPDATE emp SET salary = ? WHERE id = ?', (55000, 1))
    conn.commit()
    c.execute('SELECT * FROM emp')
    print('Updated Employees:', c.fetchall())
    conn.close()

if __name__ == '__main__':
    run()
