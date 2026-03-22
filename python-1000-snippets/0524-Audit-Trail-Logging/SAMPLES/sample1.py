# sample1.py
# Write audit events to temp/audit_0524.log.

import logging
import os

LOG_PATH = os.path.join(os.path.dirname(__file__), '../../temp/audit_0524.log')


if __name__ == '__main__':
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info('User login')
    logging.info('User viewed dashboard')
    print('Audit log written to', LOG_PATH)
