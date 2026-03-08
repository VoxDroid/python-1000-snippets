# 0084-Hash-Table Cheatsheet

- Use a fixed-size list (bucket array) and place elements by `hash(key) % size`.
- Collision resolution via chaining (each bucket is a list) or open addressing.
- Basic operations:
  ```python
  def insert(self, key, value):
      idx = self._hash(key)
      for pair in self.table[idx]:
          if pair[0] == key:
              pair[1] = value
              return
      self.table[idx].append([key, value])
  def get(self,key):
      idx = self._hash(key)
      for pair in self.table[idx]:
          if pair[0]==key: return pair[1]
      return None
  ```
- Delete by scanning bucket and removing matching key.
- Resizing (rehash) when load factor (#items/size) grows beyond threshold.
- Python’s built-in `dict` is a highly optimized hash table; re-implement only for learning.
