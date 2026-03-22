# sample3.py
# Save query result summary to temp file.

import os
import sqlite3

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0518_warehouse_summary.txt')


def main():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute('CREATE TABLE metrics (id INTEGER, value INTEGER)')
    cur.executemany('INSERT INTO metrics VALUES (?, ?)', [(1, 10), (2, 20), (3, 30)])
    cur.execute('SELECT COUNT(*), SUM(value) FROM metrics')
    count, total = cur.fetchone()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(f'count: {count}\n')
        f.write(f'total: {total}\n')
    print('Summary written to', OUTPUT_PATH)
    conn.close()


if __name__ == '__main__':
    main()
