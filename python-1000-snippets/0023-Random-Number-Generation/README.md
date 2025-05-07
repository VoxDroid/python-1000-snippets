# Random Number Generation

## Description
This snippet demonstrates generating random numbers in Python using the `random` module, useful for simulations, games, or testing.

## Code
```python
import random

integer = random.randint(1, 10)
decimal = random.uniform(0, 1)
print("Random integer:", integer)
print("Random float:", decimal)
```

## Output
```
Random integer: 7
Random float: 0.426391823456
```
*(Output varies each run)*

## Explanation
- **Random Module**: `random.randint(a, b)` generates an integer between `a` and `b` (inclusive); `random.uniform(a, b)` generates a float between `a` and `b`.
- **Import**: The `random` module must be imported to use these functions.
- **Use Case**: Random numbers are used in games (e.g., dice rolls), simulations, or shuffling data.
- **Seeding**: For reproducible results, use `random.seed(value)` before generating numbers.
- **Best Practice**: Use `secrets` module for cryptographic random numbers (e.g., passwords).