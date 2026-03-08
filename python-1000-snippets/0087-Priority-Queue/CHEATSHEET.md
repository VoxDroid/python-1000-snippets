# 0087-Priority-Queue Cheatsheet

- Use Python’s `heapq` module to build a priority queue; underlying structure is a min‑heap.
- Operations:
  - `heapq.heappush(pq, item)` – push item onto heap.
  - `heapq.heappop(pq)` – pop and return smallest item.
  - `heapq.heapify(list)` – transform list into heap in-place.
  - `heapq.heappushpop(pq,item)` – push then pop smallest.
- Store `(priority, value)` tuples; smaller priorities dequeue first.
- To support max‑heap, push `(-priority, value)` or use `heapq.nlargest`.
- Manage priority updates by pushing new tuple and ignoring stale entries when popped.
- Use `itertools.count()` to break ties or ensure stable ordering.
