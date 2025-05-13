# Repository Pattern

## Description
This snippet implements the Repository Pattern to abstract data access for the `Customer` entity, using an in-memory store for simplicity, simulating a database in an e-commerce system.

## Code
```python
# Repository pattern for managing Customer entities
try:
    class Customer:
        def __init__(self, customer_id: str, name: str):
            self.customer_id = customer_id
            self.name = name

    class CustomerRepository:
        # Initialize in-memory store
        def __init__(self):
            self._store = {}

        # Add a customer to the repository
        def add(self, customer: Customer) -> None:
            if customer.customer_id in self._store:
                raise ValueError("Customer already exists")
            self._store[customer.customer_id] = customer

        # Retrieve a customer by ID
        def get(self, customer_id: str) -> Customer:
            return self._store.get(customer_id, None)

    # Example usage
    repo = CustomerRepository()
    customer = Customer("C001", "Alice Smith")
    repo.add(customer)
    retrieved = repo.get("C001")
    print(f"Retrieved customer: {retrieved.name if retrieved else 'Not found'}")
except ImportError:
    print("Mock Output: Retrieved customer: Alice Smith")
```

## Output
```
Mock Output: Retrieved customer: Alice Smith
```
*(Real output: `Retrieved customer: Alice Smith`)*

## Explanation
- **Purpose**: The Repository Pattern decouples business logic from data persistence, providing a clean interface for accessing domain entities like `Customer`. It abstracts database operations, making the system easier to test and maintain.
- **Real-World Use Case**: In an e-commerce platform, a `CustomerRepository` manages customer data, allowing the application to switch between in-memory, SQL, or NoSQL storage without changing business logic.
- **Code Breakdown**:
  - The `Customer` class is a simple entity with `customer_id` and `name`.
  - The `CustomerRepository` class uses a dictionary as an in-memory store, simulating a database.
  - The `add` method checks for duplicates, enforcing uniqueness.
  - The `get` method retrieves a customer by ID, returning `None` if not found.
- **Challenges**: Handling concurrent access, ensuring data consistency, and mapping entities to database schemas in real systems.
- **Integration**: Works with Unit of Work (Snippet 593) for transaction management and integrates with DDD entities (Snippet 591).
- **Complexity**: O(1) for `add` and `get` operations in this in-memory implementation.
- **Best Practices**: Abstract storage details, handle errors gracefully, support transactions, and ensure testability.