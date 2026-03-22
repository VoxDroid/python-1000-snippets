# Data Validation Framework

## Description
This snippet demonstrates data validation using built-in Python checks in lieu of external libraries.

## Code
- `SAMPLES/sample1.py`: range validation for list values.
- `SAMPLES/sample2.py`: row-based validation for id/non-null/value constraints.
- `SAMPLES/sample3.py`: writes validation checks to `temp/0520_validation_report.txt`.

## Output
- sample1: `Validation completed: True`
- sample2: `Row validation: [True, False, True]`
- sample3: status file with decision results.

## Explanation
- **Data Validation Framework**: validate records before processing.
- **Logic**: apply per-row and summary checks.
- **Complexity**: O(n).
- **Use Case**: enforce data quality for ETL and analytics.
- **Best Practice**: define expectations, log failures, integrate into pipelines.
