# sample1.py
# create one table and verify it exists

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE test (id INTEGER)')
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print('Tables:', c.fetchall())
    conn.close()

if __name__ == '__main__':
    run()
