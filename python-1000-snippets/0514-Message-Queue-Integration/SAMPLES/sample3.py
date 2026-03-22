# sample3.py
# Read the log file and print count. Handles missing file gracefully.

import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0514_mq_log.txt')


if __name__ == '__main__':
    if not os.path.exists(INPUT_PATH):
        print('No log file found at', INPUT_PATH)
    else:
        with open(INPUT_PATH) as f:
            lines = [line.strip() for line in f if line.strip()]
        print('Log count:', len(lines))
