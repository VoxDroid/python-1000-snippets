# CSV Reading

## Description
This snippet shows how to read a CSV file in Python using the `csv` module, processing rows as lists or dictionaries.

## Code
```python
import csv

try:
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found.")
```

## Output
*(Assuming `data.csv` contains:)*
```
name,age,city
Alice,25,Boston
Bob,30,New York
```
```
['Alice', '25', 'Boston']
['Bob', '30', 'New York']
```

## Explanation
- **csv.reader()**: Reads the CSV file row by row, returning each row as a list.
- **With Statement**: Ensures the file is properly closed after reading.
- **Header**: `next(reader)` skips the header row.
- **Use Case**: CSV reading is used for data analysis, importing datasets, or processing tabular data.
- **Best Practice**: Use `csv.DictReader` for dictionary-based access; handle missing or malformed files.

## Additional Files
- `CHEATSHEET.md` with reader/DictReader tips and quoting rules.
- `SAMPLES/` includes:
  1. `sample1.py` – create a small CSV and read rows with `csv.reader`.
  2. `sample2.py` – read same data with `csv.DictReader`.
  3. `sample3.py` – ask for filename and column name, then output values.

Run each script in a `.venv`; samples create their own temporary files.