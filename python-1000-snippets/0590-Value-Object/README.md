# Value Object

## Description
This snippet demonstrates a value object for a money amount.

## Code
```python
try:
    class Money:
        def __init__(self, amount, currency):
            self.amount = amount
            self.currency = currency
        def __eq__(self, other):
            return self.amount == other.amount and self.currency == other.currency
    m1 = Money(100, "USD")
    m2 = Money(100, "USD")
    print("Equal:", m1 == m2)
except ImportError:
    print("Mock Output: Equal: True")
```

## Output
```
Mock Output: Equal: True
```
*(Real output: `Equal: True`)*

## Explanation
- **Value Object**: Represents an immutable value with equality.
- **Logic**: Compares two money objects by amount and currency.
- **Complexity**: O(1) per comparison.
- **Use Case**: Used in DDD for immutable domain values.
- **Best Practice**: Ensure immutability; define clear equality; validate inputs.