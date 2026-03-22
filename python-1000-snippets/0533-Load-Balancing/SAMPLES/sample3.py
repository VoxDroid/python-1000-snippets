# sample3.py
# Write load balancer selection history to temp file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0533_load_balancing.txt')


def get_server():
    from sample1 import get_server as ssh
    return ssh()


if __name__ == '__main__':
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for _ in range(5):
            s = get_server()
            f.write(s + '\n')
    print('Wrote selection history to', OUTPUT_PATH)
