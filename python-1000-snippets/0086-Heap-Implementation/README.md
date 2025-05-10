# Heap Implementation

## Description
This snippet implements a min-heap using a list, supporting insertion and extraction of the minimum element.

## Code
```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    
    def extract_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return min_val
    
    def _sift_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._sift_up(parent)
    
    def _sift_down(self, index):
        min_index = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self._sift_down(min_index)

heap = MinHeap()
heap.insert(3)
heap.insert(1)
heap.insert(4)
print("Min:", heap.extract_min())
print("Heap:", heap.heap)
```

## Output
```
Min: 1
Heap: [3, 4]
```

## Explanation
- **Min-Heap**: A binary tree where each node’s value is less than its children’s; stored as a list.
- **Methods**:
  - `insert`: Adds a value and sifts up to maintain heap property.
  - `extract_min`: Removes and returns the minimum (root); sifts down to restore heap.
- **Complexity**: O(log n) for insert/extract; O(1) for root access.
- **Use Case**: Used in priority queues, Dijkstra’s algorithm, or heap sort.
- **Best Practice**: Use Python’s `heapq` module for production; this is for learning.