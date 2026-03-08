# sample3.py
# Read comma-separated values from stdin and write them to a file

import csv
import sys

if __name__ == '__main__':
    fname = 'out3.csv'
    print('Enter CSV rows (Ctrl-D to end):')
    reader = csv.reader(sys.stdin)
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in reader:
            writer.writerow(row)
    print('wrote', fname)
