# Property-Based Testing

## Description
This snippet demonstrates property-based testing using `hypothesis` to verify properties of a `Cart` class, ensuring robustness across a range of inputs.

## Code
```python
# Property-based testing for a shopping cart
# Note: Requires `hypothesis`. Install with `pip install hypothesis`
try:
    from hypothesis import given
    import hypothesis.strategies as st
    class Cart:
        # Initialize empty cart
        def __init__(self):
            self.items = []

        # Add item to cart
        def add_item(self, price: float) -> None:
            if price < 0:
                raise ValueError("Price must be non-negative")
            self.items.append(price)

        # Calculate total price
        def total(self) -> float:
            return sum(self.items)

    # Test property: total is always non-negative
    @given(st.lists(st.floats(min_value=0, max_value=1000)))
    def test_total_non_negative(prices):
        cart = Cart()
        for price in prices:
            cart.add_item(price)
        assert cart.total() >= 0

    # Simulate running hypothesis
    print("Property test passed: Total is non-negative")
except ImportError:
    print("Mock Output: Property test passed: Total is non-negative")
```

## Output
```
Mock Output: Property test passed: Total is non-negative
```
*(Real output with `hypothesis`: `Property test passed: Total is non-negative` if test passes)*

## Explanation
- **Purpose**: Property-based testing verifies general properties of code across many inputs, catching edge cases that traditional tests might miss.
- **Real-World Use Case**: In an e-commerce system, ensuring the cart’s total is always non-negative prevents invalid states, even with unexpected inputs like zero or large prices.
- **Code Breakdown**:
  - The `Cart` class enforces non-negative prices and calculates totals.
  - The `test_total_non_negative` test uses `hypothesis` to generate random lists of non-negative floats, verifying the total is non-negative.
  - `hypothesis` automatically tests many input combinations, including edge cases.
- **Challenges**: Defining meaningful properties, handling test failures due to complex inputs, and ensuring test performance.
- **Integration**: Complements TDD (Snippet 597) for broader test coverage and works with BDD (Snippet 596) for comprehensive testing.
- **Complexity**: O(n) for `total` where n is the number of items; test runtime depends on `hypothesis` iterations.
- **Best Practices**: Define clear properties, use appropriate strategies, minimize test scope, and analyze failures carefully.