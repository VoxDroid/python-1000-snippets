# sample3.py
# Save chaos experiment metrics to temp file.

import os, random

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0538_chaos.txt'))


def run_and_log(iterations):
    stats = {'passed': 0, 'failed': 0}
    for _ in range(iterations):
        if random.random() < 0.2:
            stats['failed'] += 1
        else:
            stats['passed'] += 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(str(stats) + '\n')
    return stats


if __name__ == '__main__':
    print('Chaos stats:', run_and_log(10))
