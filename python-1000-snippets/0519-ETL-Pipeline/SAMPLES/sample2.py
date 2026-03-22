# sample2.py
# Persist ETL output to temp ETL path.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0519_etl_output.txt')


def etl_pipeline():
    raw = [1, None, 3]
    transformed = [(x if x is not None else 0) * 2 for x in raw]
    return transformed


if __name__ == '__main__':
    data = etl_pipeline()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(','.join(str(x) for x in data))
    print('Wrote ETL output to', OUTPUT_PATH)
