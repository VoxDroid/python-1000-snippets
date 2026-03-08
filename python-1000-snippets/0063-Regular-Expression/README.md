# Regular Expression

## Description
This snippet demonstrates using regular expressions to find all occurrences of a pattern (e.g., digits) in a string.

## Code
```python
import re

text = "The year is 2025 and the price is $99."
numbers = re.findall(r'\d+', text)
print("Numbers found:", numbers)
```

## Output
```
Numbers found: ['2025', '99']
```

## Explanation
- **re.findall()**: Returns all non-overlapping matches of the pattern (`\d+` for one or more digits).
- **Pattern**: `\d+` matches sequences of digits; other patterns include `\w` (word characters), `\s` (whitespace).
- **Use Case**: Regex is used for text parsing, validation, or data extraction.
- **Error Handling**: Ensure patterns are well-tested to avoid unexpected matches.
- **Best Practice**: Use raw strings (`r''`) for patterns and test regex with tools like regex101.com.

## Additional Files
- `CHEATSHEET.md` with common functions (`findall`, `search`, `match`, `sub`) and pattern examples.
- `SAMPLES/` includes:
  1. `sample1.py` – extract numbers from text.
  2. `sample2.py` – validate an email address with regex.
  3. `sample3.py` – substitute sensitive words using `re.sub`.

Run samples in a `.venv`; sample2 may read input for demonstration.