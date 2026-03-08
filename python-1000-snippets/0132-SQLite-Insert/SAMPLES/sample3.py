# sample3.py
# simulate inserting user-supplied values safely

import sqlite3

def run(name, salary):
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE emp (id INTEGER PRIMARY KEY, name TEXT, salary REAL)')
    c.execute('INSERT INTO emp (name, salary) VALUES (?, ?)', (name, salary))
    conn.commit()
    c.execute('SELECT * FROM emp')
    print(c.fetchall())
    conn.close()

if __name__ == '__main__':
    run('Charlie', 45000)
