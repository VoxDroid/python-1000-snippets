# 0085-Trie-Implementation Cheatsheet

- A trie (prefix tree) stores strings where each node corresponds to a character.
- Each node has a `children` dict mapping characters to nodes and a boolean `is_end` to mark word completions.
- Common operations:
  - `insert(word)` – adds word to trie.
  - `search(word)` – returns `True` if word exists.
  - `starts_with(prefix)` – check if any word begins with prefix.
  - `delete(word)` – optionally remove a word (needs handling of node pruning).
- Time complexity is proportional to word length (O(m)).
- Useful for autocomplete, spellcheck, dictionary lookups.
- Example prefix search implementation:
  ```python
  def starts_with(self, prefix):
      node = self.root
      for ch in prefix:
          if ch not in node.children:
              return False
          node = node.children[ch]
      return True
  ```
