# sample2.py
# delete all rows from a table

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE t(x)')
    c.executemany('INSERT INTO t(x) VALUES (?)', [(1,),(2,),(3,)])
    conn.commit()
    c.execute('DELETE FROM t')
    conn.commit()
    c.execute('SELECT COUNT(*) FROM t')
    print('count after delete', c.fetchone()[0])
    conn.close()

if __name__ == '__main__':
    run()
