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