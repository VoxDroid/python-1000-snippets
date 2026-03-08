# sample2.py
# use executemany to insert multiple entries

import sqlite3

def run():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE data (val TEXT)')
    rows = [('one',), ('two',), ('three',)]
    c.executemany('INSERT INTO data (val) VALUES (?)', rows)
    conn.commit()
    c.execute('SELECT * FROM data')
    print(c.fetchall())
    conn.close()

if __name__ == '__main__':
    run()
