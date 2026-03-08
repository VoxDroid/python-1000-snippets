# sample2.py
# Update priorities using lazy deletion technique

import heapq
import itertools

if __name__ == '__main__':
    pq = []
    counter = itertools.count()  # tie-breaker
    # insert tasks
    heapq.heappush(pq, (2, next(counter), 'task2'))
    heapq.heappush(pq, (1, next(counter), 'task1'))
    # update task2 to higher priority
    heapq.heappush(pq, (0, next(counter), 'task2'))
    # pop until we find non-stale entry
    seen = set()
    while pq:
        pr, cnt, task = heapq.heappop(pq)
        if task in seen:
            continue
        print('execute', task, 'priority', pr)
        seen.add(task)
