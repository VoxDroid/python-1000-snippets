# sample3.py
# Write anonymized record output to temp file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0522_anonymized.txt')


def anonymize_value(value):
    return '***'


if __name__ == '__main__':
    rows = [{'name': 'Alice', 'email': 'a@example.com'}, {'name': 'Bob', 'email': 'b@example.com'}]
    with open(OUTPUT_PATH, 'w') as f:
        for r in rows:
            f.write(f"{anonymize_value(r['name'])},{anonymize_value(r['email'])}\n")
    print('Wrote anonymized output to', OUTPUT_PATH)
