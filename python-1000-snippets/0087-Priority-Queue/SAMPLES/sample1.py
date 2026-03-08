# sample1.py
# Basic priority queue with heappush/heappop

import heapq

if __name__ == '__main__':
    pq = []
    heapq.heappush(pq, (2, 'task2'))
    heapq.heappush(pq, (1, 'task1'))
    heapq.heappush(pq, (3, 'task3'))
    print('pop', heapq.heappop(pq))
    print('remaining', pq)
