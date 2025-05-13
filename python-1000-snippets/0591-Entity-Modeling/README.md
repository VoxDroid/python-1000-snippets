# Entity Modeling

## Description
This snippet demonstrates entity modeling in Domain-Driven Design (DDD) by creating a `Customer` entity with identity and behavior, representing a customer in an e-commerce system.

## Code
```python
# Entity modeling for a Customer in an e-commerce domain
try:
    class Customer:
        # Initialize customer with a unique ID and name
        def __init__(self, customer_id: str, name: str):
            self._customer_id = customer_id
            self._name = name
            self._orders = []

        # Property to access customer ID (immutable identity)
        @property
        def customer_id(self) -> str:
            return self._customer_id

        # Add an order to the customer's history
        def place_order(self, order_id: str, amount: float) -> None:
            if amount <= 0:
                raise ValueError("Order amount must be positive")
            self._orders.append({"order_id": order_id, "amount": amount})

        # Calculate total order value for the customer
        def total_orders_value(self) -> float:
            return sum(order["amount"] for order in self._orders)

    # Example usage
    customer = Customer("C001", "Alice Smith")
    customer.place_order("O001", 99.99)
    print(f"Total orders value for {customer._name}: ${customer.total_orders_value():.2f}")
except ImportError:
    print("Mock Output: Total orders value for Alice Smith: $99.99")
```

## Output
```
Mock Output: Total orders value for Alice Smith: $99.99
```
*(Real output: `Total orders value for Alice Smith: $99.99`)*

## Explanation
- **Purpose**: Entity modeling in DDD defines objects with a unique identity and behavior, central to the domain. Here, the `Customer` entity encapsulates customer-specific data and logic, such as placing orders and calculating total order value, in an e-commerce context.
- **Real-World Use Case**: In an online retail platform, a `Customer` entity tracks individual customer interactions, ensuring consistent identity across transactions and enabling features like order history or loyalty programs.
- **Code Breakdown**:
  - The `Customer` class has a unique `customer_id` as its identity, immutable via a property.
  - The `place_order` method enforces domain rules (e.g., positive amount) and adds orders to an internal list.
  - The `total_orders_value` method computes the sum of order amounts, useful for analytics or reporting.
- **Challenges**: Ensuring thread-safety for concurrent order placements, validating input data robustly, and integrating with persistence layers like databases.
- **Integration**: This entity would interact with repositories (Snippet 592) for persistence and could be part of aggregates (Snippet 589) to enforce consistency.
- **Complexity**: O(1) for `place_order`, O(n) for `total_orders_value` where n is the number of orders.
- **Best Practices**: Encapsulate state, validate domain rules, use immutable identities, and align with business requirements.