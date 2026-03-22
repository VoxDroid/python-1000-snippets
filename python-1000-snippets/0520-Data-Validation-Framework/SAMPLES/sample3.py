# sample3.py
# Write validation report to temp file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0520_validation_report.txt')


def generate_report(data):
    checks = {
        'count': len(data),
        'no_nulls': all(x is not None for x in data),
        'positive': all(x >= 0 for x in data),
    }
    return checks


if __name__ == '__main__':
    data = [1, 2, 3, 4]
    report = generate_report(data)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for k, v in report.items():
            f.write(f'{k}: {v}\n')
    print('Wrote validation report to', OUTPUT_PATH)
