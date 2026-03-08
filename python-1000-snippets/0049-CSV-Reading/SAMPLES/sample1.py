# sample1.py
# create a temporary CSV file and read using csv.reader

import csv

if __name__ == '__main__':
    fname = 'temp.csv'
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'age', 'city'])
        writer.writerow(['Alice', '25', 'Boston'])
        writer.writerow(['Bob', '30', 'New York'])
    with open(fname, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        print('header:', header)
        for row in reader:
            print('row:', row)
