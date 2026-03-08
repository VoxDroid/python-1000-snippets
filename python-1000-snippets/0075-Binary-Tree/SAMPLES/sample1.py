# sample1.py
# Build a tree and print all three standard traversals

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def inorder(self, node):
        return self.inorder(node.left) + [node.data] + self.inorder(node.right) if node else []
    def preorder(self, node):
        return [node.data] + self.preorder(node.left) + self.preorder(node.right) if node else []
    def postorder(self, node):
        return self.postorder(node.left) + self.postorder(node.right) + [node.data] if node else []

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    tree = BinaryTree()
    print('in-order', tree.inorder(root))
    print('pre-order', tree.preorder(root))
    print('post-order', tree.postorder(root))
