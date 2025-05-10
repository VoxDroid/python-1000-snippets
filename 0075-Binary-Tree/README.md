# Binary Tree

## Description
This snippet implements a binary tree with a node class and a method for in-order traversal (left, root, right).

## Code
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        return result

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print("In-order Traversal:", tree.inorder_traversal(tree.root))
```

## Output
```
In-order Traversal: [4, 2, 5, 1, 3]
```

## Explanation
- **Binary Tree**: A tree where each node has at most two children (left and right).
- **In-order Traversal**: Visits nodes in the order: left subtree, root, right subtree.
- **Classes**:
  - `Node`: Stores data and pointers to left/right children.
  - `BinaryTree`: Manages the tree and provides traversal.
- **Use Case**: Binary trees are used in search trees, expression parsing, or hierarchical data.
- **Best Practice**: Implement other traversals (pre-order, post-order) and methods like insertion or deletion.