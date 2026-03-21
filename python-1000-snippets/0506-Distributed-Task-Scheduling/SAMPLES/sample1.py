# sample1.py
# Simple scheduler using sched and time modules.

import sched
import time


def task(name, duration=0.1):
    start = time.time()
    while time.time() - start < duration:
        pass
    print(f'Task {name} executed')


if __name__ == '__main__':
    scheduler = sched.scheduler(time.time, time.sleep)
    for i in range(3):
        scheduler.enter(delay=i * 0.2, priority=1, action=task, argument=(f'task{i}', 0.05))
    scheduler.run()
    print('Scheduled tasks completed')
