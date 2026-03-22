# sample2.py
# Simulate producer/consumer with queue and wal-like message log in temp.

import os
from collections import deque

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0514_mq_log.txt')


def producer(q, n=5):
    for i in range(n):
        q.append(f'event:{i}')


def consumer(q):
    processed = []
    while q:
        processed.append(q.popleft())
    return processed


if __name__ == '__main__':
    q = deque()
    producer(q, 5)
    processed = consumer(q)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write('\n'.join(processed) + '\n')
    print('Processed entries:', processed)
    print('Wrote log to', OUTPUT_PATH)
