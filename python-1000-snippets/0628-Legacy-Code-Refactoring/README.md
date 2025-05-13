# Legacy Code Refactoring

## Description
This snippet demonstrates refactoring legacy e-commerce API code to improve readability and maintainability, adding validation and documentation.

## Code
```python
# Legacy code refactoring for an API
try:
    # Legacy code
    legacy_code = """
def process_order(id, amt):
    return amt
    """

    # Refactored code
    refactored_code = """
def process_order(order_id: str, amount: float) -> float:
    '''Process an order with validation.
    
    Args:
        order_id: Unique order identifier
        amount: Order amount
    Returns:
        Validated amount
    '''
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    return amount
    """

    # Write refactored code
    with open("order.py", "w") as f:
        f.write(refactored_code)

    # Display refactored code
    print("Refactored code:", refactored_code.strip())
except ImportError:
    print("Mock Output: Refactored code: def process_order(order_id: str, amount: float) -> float:\n    '''Process an order with validation.\n    \n    Args:\n        order_id: Unique order identifier\n        amount: Order amount\n    Returns:\n        Validated amount\n    '''\n    if amount < 0:\n        raise ValueError(\"Amount must be non-negative\")\n    return amount")
```

## Output
```
Mock Output: Refactored code: def process_order(order_id: str, amount: float) -> float:
    '''Process an order with validation.
    
    Args:
        order_id: Unique order identifier
        amount: Order amount
    Returns:
        Validated amount
    '''
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    return amount
```
*(Real output: `Refactored code: <refactored code block>`)*

## Explanation
- **Purpose**: Refactoring improves legacy code’s structure, readability, and maintainability without changing functionality.
- **Real-World Use Case**: In an e-commerce system, refactoring an order processing function adds validation and documentation, making it easier to maintain and extend.
- **Code Breakdown**:
  - The legacy `process_order` function lacks validation and type hints.
  - The refactored version adds type hints, a docstring, and input validation.
  - The refactored code is saved and displayed.
- **Challenges**: Preserving functionality, writing tests for legacy code, and managing large codebases.
- **Integration**: Works with Codebase Migration (Snippet 627) and Test-Driven Development (Snippet 597) for safe refactoring.
- **Complexity**: O(n) for processing n lines of code.
- **Best Practices**: Add tests first, refactor incrementally, use linters, and document changes.