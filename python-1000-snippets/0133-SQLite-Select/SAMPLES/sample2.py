# sample2.py
# use ORDER BY and LIMIT

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE t(x INT)')
    c.executemany('INSERT INTO t(x) VALUES (?)', [(3,), (1,), (2,)])
    conn.commit()
    c.execute('SELECT x FROM t ORDER BY x DESC LIMIT 1')
    print('max', c.fetchone())
    conn.close()

if __name__ == '__main__':
    run()
