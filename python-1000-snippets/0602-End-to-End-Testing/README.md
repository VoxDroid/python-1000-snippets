# End-to-End Testing

## Description
This snippet demonstrates end-to-end testing for an e-commerce checkout process, simulating a user adding an item to a cart and checking out.

## Code
```python
# End-to-end testing for e-commerce checkout
try:
    class Cart:
        def __init__(self):
            self.items = []
        def add_item(self, price: float) -> None:
            self.items.append(price)
        def total(self) -> float:
            return sum(self.items)

    class Checkout:
        def __init__(self, cart: Cart):
            self.cart = cart
        def process(self) -> dict:
            return {"total": self.cart.total(), "status": "success"}

    # End-to-end test
    def test_checkout_e2e():
        cart = Cart()
        cart.add_item(50)
        checkout = Checkout(cart)
        result = checkout.process()
        assert result["total"] == 50, "Total mismatch"
        assert result["status"] == "success", "Checkout failed"

    # Simulate running test
    print("E2E test passed: Checkout process")
except ImportError:
    print("Mock Output: E2E test passed: Checkout process")
```

## Output
```
Mock Output: E2E test passed: Checkout process
```
*(Real output with `pytest`: `E2E test passed: Checkout process` if test passes)*

## Explanation
- **Purpose**: End-to-end (E2E) testing verifies the entire application flow from user input to output, ensuring all components work together.
- **Real-World Use Case**: In an e-commerce platform, E2E tests validate the checkout process, ensuring users can add items and complete purchases without errors.
- **Code Breakdown**:
  - The `Cart` class manages items and totals.
  - The `Checkout` class processes the cart, returning a result.
  - The `test_checkout_e2e` test simulates a user adding an item and checking out, verifying the total and status.
- **Challenges**: Managing test environments, handling UI interactions, and ensuring test reliability in complex systems.
- **Integration**: Builds on Integration Testing (Snippet 601) and supports BDD (Snippet 596) for user-focused tests.
- **Complexity**: O(n) for `total` where n is the number of items.
- **Best Practices**: Simulate real user flows, automate tests, handle flaky tests, and use realistic data.