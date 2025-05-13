# Bounded Context

## Description
This snippet demonstrates a bounded context for inventory management.

## Code
```python
try:
    class InventoryContext:
        def __init__(self):
            self.items = {}
        def add_item(self, item_id, quantity):
            self.items[item_id] = quantity
            return quantity
    inventory = InventoryContext()
    print("Added quantity:", inventory.add_item("item1", 10))
except ImportError:
    print("Mock Output: Added quantity: 10")
```

## Output
```
Mock Output: Added quantity: 10
```
*(Real output: `Added quantity: 10`)*

## Explanation
- **Bounded Context**: Isolates inventory logic in a context.
- **Logic**: Manages item quantities in a dedicated context.
- **Complexity**: O(1) per operation.
- **Use Case**: Used in DDD to separate domains.
- **Best Practice**: Define clear boundaries; avoid overlap; integrate contexts.