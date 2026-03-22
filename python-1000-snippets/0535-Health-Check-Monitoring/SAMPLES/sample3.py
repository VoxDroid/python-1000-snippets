# sample3.py
# Write health check status to temp file.

import os

# Write to repository-wide temp directory
ROOT_TEMP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp'))
OUTPUT_PATH = os.path.join(ROOT_TEMP, '0535_health_status.txt')


def write_health_status(status):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(str(status) + '\n')


if __name__ == '__main__':
    status = {'status': 'healthy', 'uptime': '10s'}
    write_health_status(status)
    print('Wrote health status to', OUTPUT_PATH)
