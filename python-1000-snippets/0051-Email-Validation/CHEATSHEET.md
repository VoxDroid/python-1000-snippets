# Email Validation Cheatsheet

## Regex Pattern
```
r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```
- `^`, `$` anchor start/end.
- Allowed user chars include `._%+-`.
- Domain can contain dots and hyphens.
- TLD requires at least 2 letters.

## Tips
- `re.match` checks from beginning; `re.fullmatch` can be used in newer Python.
- Email validation is heuristic; RFC 5322 is far more complex.

## Running samples
Activate virtual env then run `SAMPLES/sample*.py`.
