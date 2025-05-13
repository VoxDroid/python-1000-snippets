# Unit of Work

## Description
This snippet implements the Unit of Work pattern to manage transactions for `Customer` entities, ensuring atomic operations in an e-commerce system.

## Code
```python
# Unit of Work pattern for managing transactions
try:
    class Customer:
        def __init__(self, customer_id: str, name: str):
            self.customer_id = customer_id
            self.name = name

    class CustomerRepository:
        def __init__(self):
            self._store = {}
        def add(self, customer: Customer) -> None:
            self._store[customer.customer_id] = customer

    class UnitOfWork:
        # Initialize with a repository
        def __init__(self):
            self.repository = CustomerRepository()
            self._committed = False

        # Context manager for transaction
        def __enter__(self):
            return self

        # Commit changes or rollback
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is None:
                self._committed = True
            else:
                self.repository._store.clear()  # Simulate rollback

        # Add customer within transaction
        def add_customer(self, customer: Customer) -> None:
            self.repository.add(customer)

    # Example usage
    with UnitOfWork() as uow:
        customer = Customer("C001", "Alice Smith")
        uow.add_customer(customer)
    print("Transaction committed:", uow._committed)
except ImportError:
    print("Mock Output: Transaction committed: True")
```

## Output
```
Mock Output: Transaction committed: True
```
*(Real output: `Transaction committed: True`)*

## Explanation
- **Purpose**: The Unit of Work pattern tracks changes to entities and commits them atomically, ensuring data consistency across operations. It’s crucial for managing transactions in complex systems.
- **Real-World Use Case**: In an e-commerce platform, a Unit of Work ensures that adding a customer and their initial order happens atomically, preventing partial updates if an error occurs.
- **Code Breakdown**:
  - The `Customer` class is a basic entity.
  - The `CustomerRepository` manages the in-memory store.
  - The `UnitOfWork` class uses a context manager to handle transactions, committing if no exceptions occur or rolling back by clearing the store on failure.
  - The `add_customer` method adds a customer within the transaction.
- **Challenges**: Managing nested transactions, handling database-specific rollback mechanisms, and ensuring performance with large datasets.
- **Integration**: Complements Repository Pattern (Snippet 592) and integrates with DDD entities (Snippet 591).
- **Complexity**: O(1) for `add_customer`, O(n) for rollback where n is the number of stored entities.
- **Best Practices**: Ensure atomicity, minimize transaction scope, handle exceptions, and support real database transactions in production.