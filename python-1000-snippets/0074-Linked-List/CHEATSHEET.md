# 0074-Linked-List Cheatsheet

- A linked list is composed of `Node` objects with `data` and `next` attributes.
- Basic operations:
  - `append(data)` – add to end of list.
  - `display()` – traverse and collect values in Python list.
  - `insert(position, data)` – add at index (0-based).
  - `delete(data)` – remove first occurrence.
  - `search(data)` – return `True` if present.
- Example traversal:
  ```python
  current = ll.head
  while current:
      print(current.data)
      current = current.next
  ```
- Use a dummy head or handle empty list carefully when inserting/deleting.
- Linked lists are useful for dynamic collections and when frequent insertions/removals at arbitrary positions are needed.
