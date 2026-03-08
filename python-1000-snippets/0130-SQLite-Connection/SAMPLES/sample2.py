# sample2.py
# insert multiple rows using executemany

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE items (id INTEGER PRIMARY KEY, val TEXT)')
    c.executemany('INSERT INTO items (val) VALUES (?)', [('a',), ('b',), ('c',)])
    conn.commit()
    c.execute('SELECT COUNT(*) FROM items')
    print('count', c.fetchone()[0])
    conn.close()

if __name__ == '__main__':
    run()
