# sample3.py
# iterate cursor rows lazily

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE t(x)')
    c.executemany('INSERT INTO t(x) VALUES (?)', [(i,) for i in range(5)])
    conn.commit()
    c.execute('SELECT x FROM t')
    for row in c:
        print('row', row)
    conn.close()

if __name__ == '__main__':
    run()
