# sample1.py
# create a users table and insert one row

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
    c.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
    c.execute('SELECT * FROM users')
    print('Users:', c.fetchall())
    conn.close()

if __name__ == '__main__':
    run()
