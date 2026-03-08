# sample3.py
# show rowcount after deletion

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE t(x)')
    c.executemany('INSERT INTO t(x) VALUES (?)', [(1,),(2,), (3,)])
    conn.commit()
    c.execute('DELETE FROM t WHERE x = ?', (2,))
    print('deleted', c.rowcount, 'row(s)')
    conn.close()

if __name__ == '__main__':
    run()
