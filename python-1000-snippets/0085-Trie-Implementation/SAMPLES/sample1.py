# sample1.py
# Basic insertion and search

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

if __name__ == '__main__':
    trie = Trie()
    for w in ['cat', 'car', 'dog']:
        trie.insert(w)
    print('cat?', trie.search('cat'))
    print('can?', trie.search('can'))
