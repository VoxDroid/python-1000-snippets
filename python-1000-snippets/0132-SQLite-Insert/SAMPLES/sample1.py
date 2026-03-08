# sample1.py
# insert two rows and display results

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)')
    c.execute('INSERT INTO employees (name, salary) VALUES (?, ?)', ('Alice', 50000))
    c.execute('INSERT INTO employees (name, salary) VALUES (?, ?)', ('Bob', 60000))
    conn.commit()
    c.execute('SELECT * FROM employees')
    print('Employees:', c.fetchall())
    conn.close()

if __name__ == '__main__':
    run()
