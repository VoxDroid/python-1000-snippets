# Priority Queue

## Description
This snippet implements a priority queue using the `heapq` module, where elements are dequeued based on priority (smallest first).

## Code
```python
import heapq

pq = []
heapq.heappush(pq, (2, "task2"))
heapq.heappush(pq, (1, "task1"))
heapq.heappush(pq, (3, "task3"))
print("Popped:", heapq.heappop(pq))
print("Priority Queue:", pq)
```

## Output
```
Popped: (1, 'task1')
Priority Queue: [(2, 'task2'), (3, 'task3')]
```

## Explanation
- **Priority Queue**: A queue where elements are dequeued by priority (here, smallest number).
- **heapq**: Python’s module for heap operations; `heappush` adds items, `heappop` removes the smallest.
- **Tuples**: `(priority, item)` ensures heap sorts by priority.
- **Use Case**: Used in task scheduling, Dijkstra’s algorithm, or event-driven systems.
- **Best Practice**: Use `heapq` for efficient priority queues; ensure unique priorities or handle ties.