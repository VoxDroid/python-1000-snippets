# sample2.py
# read the same CSV file using DictReader

import csv

if __name__ == '__main__':
    fname = 'temp.csv'
    with open(fname, newline='') as f:
        dr = csv.DictReader(f)
        for d in dr:
            print('dict row:', d)
