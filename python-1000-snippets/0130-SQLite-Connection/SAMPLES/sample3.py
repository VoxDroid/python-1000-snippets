# sample3.py
# demonstrate parameterized queries with user input simulation

import sqlite3

def run(name):
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
    c.execute('INSERT INTO users (name) VALUES (?)', (name,))
    c.execute('SELECT name FROM users WHERE name = ?', (name,))
    print('found', c.fetchone())
    conn.close()

if __name__ == '__main__':
    run('Bob')
