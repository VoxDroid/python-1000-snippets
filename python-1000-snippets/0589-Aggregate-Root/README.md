# Aggregate Root

## Description
This snippet demonstrates an aggregate root for an order entity.

## Code
```python
try:
    class OrderAggregate:
        def __init__(self, id):
            self.id = id
            self.items = []
        def add_item(self, item):
            self.items.append(item)
            return len(self.items)
    order = OrderAggregate(1)
    print("Items in order:", order.add_item("book"))
except ImportError:
    print("Mock Output: Items in order: 1")
```

## Output
```
Mock Output: Items in order: 1
```
*(Real output: `Items in order: 1`)*

## Explanation
- **Aggregate Root**: Manages an order and its items as a single unit.
- **Logic**: Adds an item to the order aggregate.
- **Complexity**: O(1) per operation.
- **Use Case**: Used in DDD for consistency enforcement.
- **Best Practice**: Protect invariants; limit access; ensure transactional consistency.