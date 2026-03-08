# String Reversal Cheatsheet

## Slice notation for reversal
- `s[::-1]` returns reversed string.
- Works with lists and other sequences.

## Alternatives
```python
''.join(reversed(s))
```

## Tips
- Empty string returns empty.
- Reversing twice gives original: `s[::-1][::-1]`

## Running samples
Activate venv and run each sample in `SAMPLES/`.
