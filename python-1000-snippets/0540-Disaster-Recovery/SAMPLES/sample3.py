# sample3.py
# Save recovery operations to log.

import os

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0540_recovery.log'))


def log_restore(status):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'a') as f:
        f.write(status + '\n')


if __name__ == '__main__':
    log_restore('restore completed')
    print('Logged restore status to', OUTPUT_PATH)
