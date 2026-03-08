# sample2.py
# Use heap to perform heap sort

class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    def extract_min(self):
        if not self.heap:
            return None
        m = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return m
    def _sift_up(self, i):
        p = (i-1)//2
        if i>0 and self.heap[p] > self.heap[i]:
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            self._sift_up(p)
    def _sift_down(self, i):
        smallest = i
        l = 2*i+1
        r = 2*i+2
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._sift_down(smallest)

if __name__ == '__main__':
    arr = [4,1,7,3,8,5]
    h = MinHeap()
    for num in arr:
        h.insert(num)
    sorted_arr = []
    while h.heap:
        sorted_arr.append(h.extract_min())
    print('heap sorted', sorted_arr)
