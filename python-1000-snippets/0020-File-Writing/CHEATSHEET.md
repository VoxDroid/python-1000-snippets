# File Writing Cheatsheet

## Modes
- `'w'` write (overwrite)
- `'a'` append
- `'x'` create exclusive, fail if exists
- `'wb'`, `'ab'` binary modes

## Writing
```python
with open('out.txt','w') as f:
    f.write('hello')
```

## Writing multiple lines
```python
lines = ['one\n','two\n']
f.writelines(lines)
```

## Tips
- Use `os.makedirs()` to ensure directories exist.
- Always close files or use `with`.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py` (after sample1 to append)
4. `python SAMPLES/sample3.py`

