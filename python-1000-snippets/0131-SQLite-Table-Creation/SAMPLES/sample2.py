# sample2.py
# create two tables with different schemas

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE a (x INT)')
    c.execute('CREATE TABLE b (y TEXT)')
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print('Tables:', c.fetchall())
    conn.close()

if __name__ == '__main__':
    run()
