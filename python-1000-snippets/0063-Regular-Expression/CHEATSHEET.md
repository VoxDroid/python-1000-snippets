# Regular Expression Cheatsheet

## Common functions
- `re.findall(pattern, text)` -> list of all matches
- `re.search()` returns a match object for first occurrence
- `re.match()` matches only at start
- `re.sub(pattern, repl, text)` replace occurrences

## Patterns
- `\d` digit, `\w` word char, `\s` whitespace
- `+`, `*`, `?`, `{m,n}` for quantifiers
- `^` start, `$` end, `.` any char

## Tips
- Use raw string: `r"\d+"`
- Compile regex with `re.compile()` for reuse.

## Running samples
Activate venv and run `SAMPLES/sample*.py`.
