# CSV Reading Cheatsheet

## Basic reader
```python
import csv
with open('file.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

## DictReader
```python
with open('file.csv') as f:
    dr = csv.DictReader(f)
    for d in dr:
        print(d['name'])
```

## Tips
- Handle `newline=''` on open to avoid extra blank lines on Windows.
- Use `quoting=csv.QUOTE_MINIMAL` default; also QUOTE_ALL, etc.
- CSV supports different delimiters: `csv.reader(f, delimiter=';')`.

## Running samples
Activate venv and run `SAMPLES/sample*.py`.
