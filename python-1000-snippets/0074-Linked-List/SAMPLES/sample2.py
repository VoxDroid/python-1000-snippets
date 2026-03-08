# sample2.py
# Insert at head and delete a node

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
    def insert(self, pos, data):
        new_node = Node(data)
        if pos == 0 or not self.head:
            new_node.next = self.head
            self.head = new_node
            return
        idx = 0
        current = self.head
        while current.next and idx < pos-1:
            current = current.next
            idx += 1
        new_node.next = current.next
        current.next = new_node
    def delete(self, data):
        prev = None
        current = self.head
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False
    def display(self):
        elems = []
        curr = self.head
        while curr:
            elems.append(curr.data)
            curr = curr.next
        return elems

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert(1, 1.5)
    print('after insert', ll.display())
    ll.delete(2)
    print('after delete', ll.display())
