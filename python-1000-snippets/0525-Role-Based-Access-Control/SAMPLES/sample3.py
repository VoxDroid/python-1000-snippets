# sample3.py
# Log denied access events to temp.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0525_rbac_denies.log')


def log_denied(role, action):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'a') as f:
        f.write(f'{role} denied {action}\n')


if __name__ == '__main__':
    requests = [('user', 'delete'), ('guest', 'write')]
    for role, action in requests:
        log_denied(role, action)
    print('Logged denied access to', OUTPUT_PATH)
