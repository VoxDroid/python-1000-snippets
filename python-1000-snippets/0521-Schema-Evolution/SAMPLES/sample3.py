# sample3.py
# Write schema fields to temp file after evolution.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0521_schema_fields.txt')


def write_schema(fields):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for field in fields:
            f.write(field + '\n')
    return OUTPUT_PATH


if __name__ == '__main__':
    rows = [{'col1': 1}, {'col1': 2, 'col2': 3}]
    keys = sorted(set().union(*(r.keys() for r in rows)))
    path = write_schema(keys)
    print('Schema fields written to', path)
