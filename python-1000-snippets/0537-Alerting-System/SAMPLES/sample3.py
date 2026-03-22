# sample3.py
# Log alert events to file.

import os

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0537_alerts.log'))


def log_alert(message):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'a') as f:
        f.write(message + '\n')


if __name__ == '__main__':
    log_alert('CPU usage high')
    print('Logged alert to', OUTPUT_PATH)
