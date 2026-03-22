# ETL Pipeline

## Description
This snippet demonstrates a simple ETL pipeline using pure Python operations.

## Code
- `SAMPLES/sample1.py`: extract/transform/load in memory with missing values handling.
- `SAMPLES/sample2.py`: writes output to `temp/0519_etl_output.txt`.
- `SAMPLES/sample3.py`: writes ETL step stats to `temp/0519_etl_stats.txt`.

## Output
- sample1: `ETL result: [2, 0, 6]`
- sample2: output file with transformed values.
- sample3: stats file with counts and sum.

## Explanation
- **ETL Pipeline**: data flow from source to target.
- **Logic**: fill missing with default and apply transformation.
- **Complexity**: O(n) where n is records.
- **Use Case**: data engineering tasks.
- **Best Practice**: use schema validation and log statuses.
