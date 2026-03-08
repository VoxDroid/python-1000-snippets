# sample3.py
# Level-order traversal of a binary tree using BFS

from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result

if __name__ == '__main__':
    # build tree:   1
    #             /   \
    #            2     3
    root = Node(1, Node(2), Node(3))
    print('levels', level_order(root))
