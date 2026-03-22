# sample3.py
# Append a specific audit event and verify commit.

import logging
import os

LOG_PATH = os.path.join(os.path.dirname(__file__), '../../temp/audit_0524.log')


if __name__ == '__main__':
    logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info('User performed sensitive action')
    print('Appended sensitive action to audit log')
