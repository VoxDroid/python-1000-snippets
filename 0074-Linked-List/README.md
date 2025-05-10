# Linked List

## Description
This snippet implements a singly linked list with methods to append nodes and print the list.

## Code
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print("Linked List:", ll.display())
```

## Output
```
Linked List: [1, 2, 3]
```

## Explanation
- **Linked List**: A linear data structure where each node contains data and a reference to the next node.
- **Classes**:
  - `Node`: Stores data and a `next` pointer.
  - `LinkedList`: Manages nodes with `append` (adds to the end) and `display` (returns list of values).
- **Use Case**: Linked lists are used when dynamic size or frequent insertions are needed (e.g., implementing stacks or queues).
- **Best Practice**: Add methods for deletion or insertion at specific positions; handle edge cases like empty lists.