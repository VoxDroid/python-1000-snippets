# sample3.py
# Write backup snapshot info to file.

import os

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0541_backup_snapshot.txt'))


def save_snapshot(info):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(info + '\n')


if __name__ == '__main__':
    save_snapshot('snapshot taken')
    print('Saved snapshot to', OUTPUT_PATH)
