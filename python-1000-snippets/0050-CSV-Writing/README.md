# CSV Writing

## Description
This snippet demonstrates writing data to a CSV file in Python using the `csv` module, creating a structured tabular file.

## Code
```python
import csv

data = [
    ["name", "age", "city"],
    ["Alice", 25, "Boston"],
    ["Bob", 30, "New York"]
]
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
print("CSV file written successfully.")
```

## Output
```
CSV file written successfully.
```
*(Creates `output.csv` with:)*
```
name,age,city
Alice,25,Boston
Bob,30,New York
```

## Explanation
- **csv.writer()**: Writes rows to the CSV file as comma-separated values.
- **newline=""**: Prevents extra blank lines in the CSV file (Python 3).
- **With Statement**: Ensures the file is properly closed after writing.
- **Use Case**: CSV writing is used for exporting data, generating reports, or saving datasets.
- **Best Practice**: Use `csv.DictWriter` for dictionary-based data; handle file permissions errors.

## Additional Files
- `CHEATSHEET.md` with writer/DictWriter tips and newline notes.
- `SAMPLES/` contains:
  1. `sample1.py` – write a list-of-lists to CSV.
  2. `sample2.py` – use `csv.DictWriter` to output dictionaries.
  3. `sample3.py` – read rows from stdin and write to file.

Run samples inside a `.venv`; they will create output files.