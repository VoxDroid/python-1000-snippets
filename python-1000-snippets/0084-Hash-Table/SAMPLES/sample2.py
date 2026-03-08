# sample2.py
# Demonstrate key update and deletion

class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]
    def _hash(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[idx].append([key, value])
    def get(self, key):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                return pair[1]
        return None
    def delete(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return True
        return False

if __name__ == '__main__':
    ht = HashTable()
    ht.insert('a',1)
    ht.insert('a',2)
    print('updated a ->', ht.get('a'))
    ht.delete('a')
    print('after delete a ->', ht.get('a'))
