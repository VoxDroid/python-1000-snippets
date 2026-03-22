# sample2.py
# Run filtering query and output results list.

import sqlite3


def main():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute('CREATE TABLE inventory (id INTEGER PRIMARY KEY, quantity INTEGER)')
    cur.executemany('INSERT INTO inventory (quantity) VALUES (?)', [(5,), (10,), (0,), (30,)])
    cur.execute('SELECT quantity FROM inventory WHERE quantity > 5')
    rows = [r[0] for r in cur.fetchall()]
    print('Filtered quantities >5:', rows)
    conn.close()


if __name__ == '__main__':
    main()
