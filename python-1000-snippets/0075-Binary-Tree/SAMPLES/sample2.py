# sample2.py
# Simple binary search tree insert and search

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        self._insert(self.root, value)
    def _insert(self, node, value):
        if value < node.data:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)
    def search(self, value):
        return self._search(self.root, value)
    def _search(self, node, value):
        if not node:
            return False
        if node.data == value:
            return True
        return self._search(node.left, value) if value < node.data else self._search(node.right, value)

if __name__ == '__main__':
    bst = BST()
    for v in [7, 3, 9, 1, 5]:
        bst.insert(v)
    print('search 5?', bst.search(5))
    print('search 8?', bst.search(8))
