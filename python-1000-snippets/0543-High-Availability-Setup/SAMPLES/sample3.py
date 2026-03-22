# sample3.py
# Save HA configuration status to temp file.

import os

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0543_ha.txt'))


def save_ha_status(status):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(status + '\n')


if __name__ == '__main__':
    save_ha_status('high availability enabled')
    print('Saved HA status to', OUTPUT_PATH)
