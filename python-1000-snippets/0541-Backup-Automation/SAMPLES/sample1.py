# sample1.py
# Backup a sample file using shutil.

import os
import shutil

SOURCE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0541_data.txt'))
DEST = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0541_data_backup.txt'))


def create_source():
    os.makedirs(os.path.dirname(SOURCE), exist_ok=True)
    with open(SOURCE, 'w') as f:
        f.write('important data')


def backup_file():
    create_source()
    shutil.copy(SOURCE, DEST)
    return os.path.exists(DEST)


if __name__ == '__main__':
    print('Backup successful:', backup_file())
