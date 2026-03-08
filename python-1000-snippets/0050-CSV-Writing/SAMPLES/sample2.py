# sample2.py
# Use DictWriter to output dictionary records

import csv

if __name__ == '__main__':
    fieldnames = ['name', 'age']
    rows = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
    with open('out2.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print('wrote out2.csv')
