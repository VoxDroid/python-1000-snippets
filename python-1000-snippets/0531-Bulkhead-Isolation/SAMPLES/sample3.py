# sample3.py
# Log bulkhead sessions with simple text output.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0531_bulkhead_log.txt')


def log_bulkhead(s):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'a') as f:
        f.write(s + '\n')


if __name__ == '__main__':
    log_bulkhead('Bulkhead api max=2 used=1')
    log_bulkhead('Bulkhead db max=1 used=0')
    print('Written bulkhead log to', OUTPUT_PATH)
