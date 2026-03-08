# Reduce Function

## Description
This snippet demonstrates the `reduce()` function from the `functools` module, which applies a function cumulatively to an iterable to reduce it to a single value.

## Code
```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)
```

## Output
```
Product: 24
```

## Explanation
- **Reduce Function**: `reduce(function, iterable)` applies `function` to pairs of items, accumulating the result (e.g., `1*2=2`, `2*3=6`, `6*4=24`).
- **Lambda**: `lambda x, y: x * y` multiplies two numbers.
- **Import**: `reduce` requires importing from `functools`.
- **Use Case**: `reduce()` is used for operations like summing, multiplying, or concatenating lists.
- **Best Practice**: Use `reduce()` for functional programming; built-in functions like `sum()` may be clearer for common tasks.

## Additional Files
- `CHEATSHEET.md` containing quick reduce examples and alternatives.
- `SAMPLES/` with:
  1. `sample1.py` – compute product as shown.
  2. `sample2.py` – sum numbers with initializer.
  3. `sample3.py` – concatenate strings from a list.

Run samples in a `.venv` to observe behavior.