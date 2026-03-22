# sample3.py
# Write risk analysis report to temp.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0559_risk.txt'))


def save_risk_report(report):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(str(report) + '\n')
    return OUTPUT


if __name__ == '__main__':
    report = {'risk_score': 1.7, 'risk_level': 'medium'}
    path = save_risk_report(report)
    print('Saved report to', path)
    with open(path) as f:
        print(f.read().strip())
