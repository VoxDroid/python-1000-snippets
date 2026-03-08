# sample1.py
# Basic hash table insert/get

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    def _hash(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

if __name__ == '__main__':
    ht = HashTable()
    ht.insert('apple', 5)
    ht.insert('banana', 8)
    print('apple ->', ht.get('apple'))
    print('banana ->', ht.get('banana'))
