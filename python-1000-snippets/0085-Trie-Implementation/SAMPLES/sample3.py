# sample3.py
# Delete words from trie and confirm removal

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
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
    def delete(self, word, node=None, depth=0):
        if node is None:
            node = self.root
        if depth == len(word):
            if not node.is_end:
                return False
            node.is_end = False
            return len(node.children) == 0
        ch = word[depth]
        if ch not in node.children:
            return False
        should_delete = self.delete(word, node.children[ch], depth+1)
        if should_delete:
            del node.children[ch]
            return not node.is_end and len(node.children) == 0
        return False

if __name__ == '__main__':
    trie = Trie()
    trie.insert('hi')
    trie.insert('hit')
    print('search hi', trie.search('hi'))
    trie.delete('hit')
    print('search hit after delete', trie.search('hit'))
    trie.delete('hi')
    print('search hi after delete', trie.search('hi'))
