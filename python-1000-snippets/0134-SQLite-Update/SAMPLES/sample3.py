# sample3.py
# use WHERE clause to update specific rows only

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE items (id INTEGER PRIMARY KEY, qty INTEGER)')
    c.executemany('INSERT INTO items (qty) VALUES (?)', [(5,), (10,), (15,)])
    conn.commit()
    c.execute('UPDATE items SET qty = ? WHERE qty > ?', (20, 8))
    conn.commit()
    c.execute('SELECT * FROM items')
    print('Items:', c.fetchall())
    conn.close()

if __name__ == '__main__':
    run()
