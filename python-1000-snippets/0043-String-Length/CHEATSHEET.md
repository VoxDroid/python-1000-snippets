# String Length Cheatsheet

## Using `len()` on strings
- Counts code points, not grapheme clusters.
- Includes spaces, punctuation, and combining characters.

## Tips
- `'a\n'.__len__()` returns 2 (newline counted).
- For byte length, use `len(s.encode('utf-8'))`.

## Example
```python
if len(s) == 0:
    print('empty string')
```

## Running samples
Activate virtual env and run the sample scripts in `SAMPLES/`.
