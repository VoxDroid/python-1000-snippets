# sample3.py
# Log fraud alerts to temp file.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0558_fraud.txt'))


def save_alerts(alerts):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        for alert in alerts:
            f.write(str(alert) + '\n')
    return OUTPUT


if __name__ == '__main__':
    alerts = [{'id': 2,'reason':'large amount'}]
    path = save_alerts(alerts)
    print('Saved alerts to', path)
    with open(path) as f:
        print(f.read().strip())
