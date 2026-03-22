# sample1.py
# Create an SQLite table and run a sum aggregation query.

import sqlite3


def main():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute('CREATE TABLE sales (id INTEGER PRIMARY KEY, amount INTEGER)')
    cur.executemany('INSERT INTO sales (amount) VALUES (?)', [(100,), (200,), (300,)])
    cur.execute('SELECT SUM(amount) FROM sales')
    total = cur.fetchone()[0]
    print('Total sales:', total)
    conn.close()


if __name__ == '__main__':
    main()
