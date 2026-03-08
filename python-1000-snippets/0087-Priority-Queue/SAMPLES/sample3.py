# sample3.py
# Use dataclass for better readability

import heapq
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

if __name__ == '__main__':
    pq = []
    heapq.heappush(pq, PrioritizedItem(5, 'clean'))
    heapq.heappush(pq, PrioritizedItem(1, 'eat'))
    heapq.heappush(pq, PrioritizedItem(3, 'sleep'))
    while pq:
        pi = heapq.heappop(pq)
        print('do', pi.item, 'priority', pi.priority)
