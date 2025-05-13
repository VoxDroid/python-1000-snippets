# Domain-Driven Design

## Description
This snippet demonstrates a DDD entity with domain logic.

## Code
```python
try:
    class Order:
        def __init__(self, id):
            self.id = id
            self.status = "pending"
        def confirm(self):
            self.status = "confirmed"
            return self.status
    order = Order(1)
    print("Order status:", order.confirm())
except ImportError:
    print("Mock Output: Order status: confirmed")
```

## Output
```
Mock Output: Order status: confirmed
```
*(Real output: `Order status: confirmed`)*

## Explanation
- **Domain-Driven Design**: Models domain logic in an entity.
- **Logic**: Represents an order with a confirm action.
- **Complexity**: O(1) per operation.
- **Use Case**: Used in complex business applications.
- **Best Practice**: Encapsulate logic; define clear boundaries; align with domain.