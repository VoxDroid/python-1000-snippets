# sample3.py
# Log data lake path and existence status to temp.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0517_data_lake_status.txt')
CSV_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0517_data_lake.csv')
PARQUET_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0517_data_lake.parquet')


if __name__ == '__main__':
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(f'csv_exists: {os.path.exists(CSV_PATH)}\n')
        f.write(f'parquet_exists: {os.path.exists(PARQUET_PATH)}\n')
    print('Wrote data lake status to', OUTPUT_PATH)
