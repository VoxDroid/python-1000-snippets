# Trie Implementation

## Description
This snippet implements a trie (prefix tree) to store and search strings efficiently.

## Code
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

trie = Trie()
trie.insert("cat")
trie.insert("car")
print("Search 'cat':", trie.search("cat"))
print("Search 'can':", trie.search("can"))
```

## Output
```
Search 'cat': True
Search 'can': False
```

## Explanation
- **Trie**: A tree where each node represents a character, with paths forming words; `is_end` marks word endings.
- **Methods**:
  - `insert`: Adds a word by creating nodes for each character.
  - `search`: Checks if a word exists in the trie.
- **Use Case**: Used in autocomplete, spell checkers, or prefix-based searches.
- **Complexity**: O(m) time for insert/search, where m is word length.
- **Best Practice**: Add prefix search or deletion methods for full functionality.