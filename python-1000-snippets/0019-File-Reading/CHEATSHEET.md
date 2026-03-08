# File Reading Cheatsheet

## Modes
- `'r'` read text
- `'rb'` read binary

## Methods
- `read()` reads entire file
- `readline()` reads one line
- `readlines()` returns list of lines

## Example
```python
with open('file.txt', 'r') as f:
    for line in f:
        print(line, end='')
```

## Tips
- Use `with` to auto-close files.
- Specify encoding: `open('file.txt','r',encoding='utf-8')`.

## Running samples
1. Create a text file `example.txt` in the same folder.
2. `python3 -m venv .venv && source .venv/bin/activate`
3. `python SAMPLES/sample1.py`
4. `python SAMPLES/sample2.py`
5. `python SAMPLES/sample3.py`

