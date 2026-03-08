# sample3.py
# prompt for file and column, then print values from that column

import csv

if __name__ == '__main__':
    fname = input('CSV filename (temp.csv): ') or 'temp.csv'
    col = input('Column name: ')
    try:
        with open(fname, newline='') as f:
            dr = csv.DictReader(f)
            for d in dr:
                print(d.get(col))
    except FileNotFoundError:
        print('file not found')
