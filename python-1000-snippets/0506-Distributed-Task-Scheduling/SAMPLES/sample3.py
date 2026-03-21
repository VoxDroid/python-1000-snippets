# sample3.py
# Record scheduled/done jobs into temp log file.

import os
import sched
import time

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0506_distributed_schedule.txt')


def worker(name):
    print(f'Running {name}')
    return f'{name}-done'


if __name__ == '__main__':
    scheduler = sched.scheduler(time.time, time.sleep)
    results = []
    for i in range(4):
        scheduler.enter(i*0.1, 1, lambda n=i: results.append(worker(f'job{n}')))

    scheduler.run()

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(''.join(r + '\n' for r in results))

    print('Wrote distributed schedule info to', OUTPUT_PATH)
