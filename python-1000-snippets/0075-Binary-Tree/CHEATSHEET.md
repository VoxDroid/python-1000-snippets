# 0075-Binary-Tree Cheatsheet

- Each node has `data`, `left`, and `right` attributes.
- Common traversals:
  ```python
  def inorder(n):
      return inorder(n.left) + [n.data] + inorder(n.right) if n else []
  def preorder(n):
      return [n.data] + preorder(n.left) + preorder(n.right) if n else []
  def postorder(n):
      return postorder(n.left) + postorder(n.right) + [n.data] if n else []
  ```
- To build a binary search tree (BST), insert smaller values to the left, larger to the right.
- Utility methods:
  - `height(node)` returns tree height.
  - `search(node,data)` returns boolean.
- Use recursion or stack for traversals; iterative versions use an explicit stack.
- Binary trees are foundations for search trees, heaps, expression parsing.
