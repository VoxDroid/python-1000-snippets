# sample2.py
# Read back the data lake CSV and print row count.

import csv
import os

INPUT_CSV = os.path.join(os.path.dirname(__file__), '../../temp/0517_data_lake.csv')


if __name__ == '__main__':
    if not os.path.exists(INPUT_CSV):
        print('CSV not found:', INPUT_CSV)
    else:
        with open(INPUT_CSV, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        print('Row count in CSV:', len(rows))
