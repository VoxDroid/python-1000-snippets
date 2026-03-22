# sample1.py
# Simulate writing data lake record as CSV and optional parquet via pyarrow.

import csv
import os

OUTPUT_CSV = os.path.join(os.path.dirname(__file__), '../../temp/0517_data_lake.csv')


def write_csv(data, path=OUTPUT_CSV):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'value'])
        writer.writeheader()
        writer.writerows(data)
    return path


def write_parquet(path):
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq
        table = pa.Table.from_pydict({'id': [1, 2, 3], 'value': [1, 2, 3]})
        pq.write_table(table, path)
        return 'parquet-written'
    except Exception as e:
        return f'parquet not written: {e}'


if __name__ == '__main__':
    csv_path = write_csv([{'id': 1, 'value': 1}, {'id': 2, 'value': 2}, {'id': 3, 'value': 3}])
    print('CSV written:', csv_path)
    print(write_parquet(os.path.join(os.path.dirname(__file__), '../../temp/0517_data_lake.parquet')))
