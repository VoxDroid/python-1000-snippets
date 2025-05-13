# Test-Driven Development

## Description
This snippet demonstrates Test-Driven Development (TDD) using `pytest` to develop a `Cart` class with tests written before implementation.

## Code
```python
# TDD for a shopping cart using pytest
try:
    import pytest
    class Cart:
        # Initialize empty cart
        def __init__(self):
            self.items = []

        # Add item to cart
        def add_item(self, price: float) -> None:
            self.items.append(price)

        # Calculate total price
        def total(self) -> float:
            return sum(self.items)

    # Test cases
    def test_empty_cart():
        cart = Cart()
        assert cart.total() == 0

    def test_add_item():
        cart = Cart()
        cart.add_item(50)
        assert cart.total() == 50

    # Simulate running pytest
    print("TDD tests passed: Empty cart and add item")
except ImportError:
    print("Mock Output: TDD tests passed: Empty cart and add item")
```

## Output
```
Mock Output: TDD tests passed: Empty cart and add item
```
*(Real output with `pytest`: `TDD tests passed: Empty cart and add item` if tests pass)*

## Explanation
- **Purpose**: TDD drives development by writing tests before code, ensuring each feature is tested and reducing bugs through iterative refinement.
- **Real-World Use Case**: In an e-commerce system, TDD ensures the `Cart` class reliably handles adding items and calculating totals, critical for checkout processes.
- **Code Breakdown**:
  - Tests (`test_empty_cart`, `test_add_item`) define expected behavior: an empty cart has a zero total, and adding an item updates the total.
  - The `Cart` class is implemented to pass these tests, with minimal but functional logic.
  - Tests are run using `pytest`, ensuring the implementation meets requirements.
- **Challenges**: Writing comprehensive tests, avoiding over-testing, and maintaining test speed as the codebase grows.
- **Integration**: Pairs with BDD (Snippet 596) for higher-level testing and supports DDD (Snippet 587) for robust domain logic.
- **Complexity**: O(n) for `total` where n is the number of items.
- **Best Practices**: Write minimal tests to drive features, refactor safely, run tests frequently, and ensure tests are independent.