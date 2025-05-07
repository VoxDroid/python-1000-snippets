# Temperature Conversion

## Description
This snippet converts temperatures between Celsius and Fahrenheit using a function, demonstrating basic mathematical operations and user input.

## Code
```python
def convert_temperature(value, unit):
    if unit == "C":
        return (value * 9/5) + 32
    elif unit == "F":
        return (value - 32) * 5/9
    else:
        return "Invalid unit"

value = float(input("Enter temperature: "))
unit = input("Enter unit (C or F): ").upper()
result = convert_temperature(value, unit)
print(f"Result: {result} {'F' if unit == 'C' else 'C'}")
```

## Output
```
Enter temperature: 25
Enter unit (C or F): C
Result: 77.0 F
```

## Explanation
- **Function**: `convert_temperature(value, unit)` converts based on the unit (`C` for Celsius to Fahrenheit, `F` for Fahrenheit to Celsius).
- **Formulas**: Celsius to Fahrenheit: `(C * 9/5) + 32`; Fahrenheit to Celsius: `(F - 32) * 5/9`.
- **Input Handling**: Converts unit to uppercase for case-insensitive input.
- **Use Case**: Useful for weather apps or scientific calculations.
- **Best Practice**: Validate numeric input and handle edge cases (e.g., extreme temperatures).