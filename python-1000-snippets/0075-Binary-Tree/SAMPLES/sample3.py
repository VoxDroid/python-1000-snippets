# sample3.py
# Compute height of binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    print('height', height(root))
