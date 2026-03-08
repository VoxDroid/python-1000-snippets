# sample3.py
# Convert linked list to Python list and search

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
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    def to_list(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.data)
            curr = curr.next
        return lst
    def search(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

if __name__ == '__main__':
    ll = LinkedList()
    for ch in 'hello':
        ll.append(ch)
    print('as list', ll.to_list())
    print('search l?', ll.search('l'))
    print('search z?', ll.search('z'))
