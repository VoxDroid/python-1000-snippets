# sample3.py
# Verify GDPR deletions by checking audit log entries.

import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0523_gdpr_deletions.log')


if __name__ == '__main__':
    if not os.path.exists(INPUT_PATH):
        print('No GDPR log file found')
    else:
        lines = [line.strip() for line in open(INPUT_PATH) if line.strip()]
        print('Deletion count:', len(lines))
