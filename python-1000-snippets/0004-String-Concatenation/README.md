# String Concatenation

## Description
This snippet shows how to combine (concatenate) strings in Python using the `+` operator and f-strings. String concatenation is useful for creating dynamic messages or formatting text.

## Code
```python
first_name = "John"
last_name = "Doe"
greeting = "Hello, " + first_name + " " + last_name + "!"
f_greeting = f"Hello, {first_name} {last_name}!"
print(greeting)
print(f_greeting)
```

## Output
```
Hello, John Doe!
Hello, John Doe!
```

## Explanation
- **Concatenation with `+`**: The `+` operator joins strings together. Spaces or punctuation must be explicitly included (e.g., `" "` for a space).
- **f-strings**: Introduced in Python 3.6, f-strings (`f"..."`) provide a more readable way to embed variables directly within strings.
- **Variables**: `first_name` and `last_name` store string values that are combined to form a greeting.
- **Use Case**: String concatenation is used in user interfaces, logging, or generating dynamic content like emails or reports.
- **Best Practice**: f-strings are preferred over `+` for concatenation due to better readability and performance when combining multiple strings.

## Additional Files
- `CHEATSHEET.md` includes operator summaries, `join()` tips, and examples.
- `SAMPLES/` contains three scripts:
  1. `sample1.py` – greeting construction.
  2. `sample2.py` – build a comma-separated list from input.
  3. `sample3.py` – demonstrate safe path concatenation.

Run samples under a `.venv` to verify behavior.