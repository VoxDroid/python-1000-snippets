# sample2.py
# Read the audit log and count entries.

import os

LOG_PATH = os.path.join(os.path.dirname(__file__), '../../temp/audit_0524.log')


if __name__ == '__main__':
    if not os.path.exists(LOG_PATH):
        print('Audit log missing')
    else:
        with open(LOG_PATH) as f:
            lines = [line.strip() for line in f if line.strip()]
        print('Audit events count:', len(lines))
