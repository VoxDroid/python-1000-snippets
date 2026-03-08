# sample3.py
# Force collisions by using small table size

class HashTable:
    def __init__(self, size=2):
        self.size = size
        self.table = [[] for _ in range(size)]
    def _hash(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        idx = self._hash(key)
        self.table[idx].append([key, value])
    def display(self):
        return self.table

if __name__ == '__main__':
    ht = HashTable()
    words = ['apple','banana','grape','cherry']
    for w in words:
        ht.insert(w, len(w))
    print('table with collisions', ht.display())
