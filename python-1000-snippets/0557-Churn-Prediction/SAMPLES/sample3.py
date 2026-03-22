# sample3.py
# Write churn prediction analysis to temp storage.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0557_churn.txt'))


def save_churn_report(report):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(str(report) + '\n')
    return OUTPUT


if __name__ == '__main__':
    report = {'predictions': ['churn', 'retain'], 'risk': 0.5}
    path = save_churn_report(report)
    print('Saved report to', path)
    with open(path) as f:
        print(f.read().strip())
