# Tax Calculation

## Description
This snippet demonstrates calculating sales tax for an e-commerce order based on the customer’s location.

## Code
```python
# Tax calculation for orders
try:
    # Simulated tax rates by state
    TAX_RATES = {
        "CA": 0.0875,  # California tax rate
        "NY": 0.08875  # New York tax rate
    }

    # Calculate tax for an order
    def calculate_tax(amount: float, state: str) -> float:
        # Get tax rate or default to 0
        tax_rate = TAX_RATES.get(state, 0)
        # Calculate tax amount
        tax = amount * tax_rate
        return round(tax, 2)

    # Example usage
    result = calculate_tax(100.00, "CA")
    print("Tax calculated:", result)
except ImportError:
    print("Mock Output: Tax calculated: 8.75")
```

## Output
```
Mock Output: Tax calculated: 8.75
```
*(Real output: `Tax calculated: 8.75`)*

## Explanation
- **Purpose**: Tax calculation applies the correct sales tax based on jurisdiction, ensuring compliance with tax laws.
- **Real-World Use Case**: In an e-commerce platform, calculating tax for orders in different states ensures accurate checkout totals and tax filings.
- **Code Breakdown**:
  - A dictionary stores tax rates by state.
  - The `calculate_tax` function multiplies the order amount by the state’s tax rate, rounding to two decimals.
  - The output shows the calculated tax.
- **Challenges**: Managing varying tax rates, handling exemptions, and integrating with tax services like Avalara.
- **Integration**: Complements Payment Gateway Integration (Snippet 651) and Compliance Reporting (Snippet 656) for financial compliance.
- **Complexity**: O(1) for tax calculation.
- **Best Practices**: Use external tax services, update rates regularly, log calculations, and handle edge cases like tax-exempt customers.