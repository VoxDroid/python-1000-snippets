# sample2.py
# Log deletion events to a temp audit file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0523_gdpr_deletions.log')


def log_deletion(user_id):
    with open(OUTPUT_PATH, 'a') as f:
        f.write(f'user_id {user_id} deleted\n')


if __name__ == '__main__':
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    log_deletion(1)
    log_deletion(2)
    print('Deletion events logged to', OUTPUT_PATH)
