# 0086-Heap-Implementation Cheatsheet

- Heap is a complete binary tree stored in list form: parent at index `i`, children at `2*i+1` and `2*i+2`.
- Min-heap property: every parent value ≤ child values.
- Primary operations:
  - `insert(value)` – add at end and sift up.
  - `extract_min()` – remove root, replace with last element, sift down.
- Can build heap from list in O(n) using `heapify` (sift-down from middle).
- For max-heap, invert comparisons or store negative values.
- Useful for priority queues; Python’s `heapq` provides `heappush`, `heappop`, and `heapify`.
