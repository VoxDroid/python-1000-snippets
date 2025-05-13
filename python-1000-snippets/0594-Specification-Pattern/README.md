# Specification Pattern

## Description
This snippet implements the Specification Pattern to define reusable business rules for filtering `Customer` entities, such as identifying premium customers based on order history.

## Code
```python
# Specification pattern for defining business rules
try:
    class Customer:
        def __init__(self, customer_id: str, total_spent: float):
            self.customer_id = customer_id
            self.total_spent = total_spent

    class Specification:
        # Abstract base for specifications
        def is_satisfied_by(self, candidate) -> bool:
            raise NotImplementedError

    class PremiumCustomerSpecification(Specification):
        # Define premium customer as spending over $500
        def is_satisfied_by(self, customer: Customer) -> bool:
            return customer.total_spent > 500

    # Example usage
    customer = Customer("C001", 600)
    spec = PremiumCustomerSpecification()
    print("Is premium customer:", spec.is_satisfied_by(customer))
except ImportError:
    print("Mock Output: Is premium customer: True")
```

## Output
```
Mock Output: Is premium customer: True
```
*(Real output: `Is premium customer: True`)*

## Explanation
- **Purpose**: The Specification Pattern encapsulates business rules as reusable, composable objects, making it easy to apply domain logic consistently across the application.
- **Real-World Use Case**: In an e-commerce system, this pattern could identify premium customers for special offers or prioritize support tickets based on customer attributes.
- **Code Breakdown**:
  - The `Customer` class includes `total_spent` to track spending.
  - The `Specification` base class defines the interface for rules.
  - The `PremiumCustomerSpecification` implements a rule for customers spending over $500.
  - The `is_satisfied_by` method evaluates the rule against a customer.
- **Challenges**: Combining multiple specifications (e.g., AND/OR logic), maintaining performance with complex rules, and ensuring rules are testable.
- **Integration**: Works with Repository Pattern (Snippet 592) to filter entities and aligns with DDD principles (Snippet 587).
- **Complexity**: O(1) for `is_satisfied_by` in this simple case.
- **Best Practices**: Keep specifications focused, support composition, test rules thoroughly, and document business intent.