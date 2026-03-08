# sample1.py
# Write a simple table to CSV using csv.writer

import csv

if __name__ == '__main__':
    data = [
        ['name', 'age', 'city'],
        ['Alice', 25, 'Boston'],
        ['Bob', 30, 'New York']
    ]
    with open('out1.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print('wrote out1.csv')
