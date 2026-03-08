# Palindrome Check Cheatsheet

## Cleaning
```python
s = ''.join(c.lower() for c in s if c.isalnum())
```

## Check palindrome
```python
return s == s[::-1]
```

## Tips
- Use `s[::-1]` to reverse string.
- Remove spaces and punctuation before checking.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py` (input required)
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

