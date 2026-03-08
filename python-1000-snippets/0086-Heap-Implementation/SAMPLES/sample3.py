# sample3.py
# Priority queue with (priority, item) tuples

import heapq

if __name__ == '__main__':
    pq = []
    for priority, task in [(2,'clean'),(1,'eat'),(3,'sleep')]:
        heapq.heappush(pq, (priority, task))
    while pq:
        pr, t = heapq.heappop(pq)
        print('do', t, 'with priority', pr)
