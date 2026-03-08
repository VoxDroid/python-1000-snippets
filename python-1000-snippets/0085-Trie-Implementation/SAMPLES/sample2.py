# sample2.py
# Add prefix search (starts_with)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

if __name__ == '__main__':
    trie = Trie()
    for w in ['apple','banana','grape']:
        trie.insert(w)
    print('starts with ap', trie.starts_with('ap'))
    print('starts with ba', trie.starts_with('ba'))
    print('starts with gr', trie.starts_with('gr'))
    print('starts with xy', trie.starts_with('xy'))
