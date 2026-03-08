# sample2.py
# increase all salaries by 10%

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE emp (id INTEGER PRIMARY KEY, salary REAL)')
    c.executemany('INSERT INTO emp (salary) VALUES (?)', [(50000,), (60000,)])
    conn.commit()
    c.execute('UPDATE emp SET salary = salary * 1.1')
    conn.commit()
    c.execute('SELECT salary FROM emp')
    print('New salaries:', c.fetchall())
    conn.close()

if __name__ == '__main__':
    run()
