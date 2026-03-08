# CSV Writing Cheatsheet

## Using csv.writer
```python
with open('out.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['a','b'])
```

## Using csv.DictWriter
```python
with open('out.csv','w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=['name','age'])
    w.writeheader()
    w.writerow({'name':'Alice','age':30})
```

## Tips
- Include `newline=''` to avoid blank lines.
- `writerows()` can write multiple rows at once.
- Choose delimiter, quoting as needed.

## Running samples
Activate venv and run `SAMPLES/sample*.py`.
