# Data Lake Integration

## Description
This snippet demonstrates data lake integration via local CSV write/read and optional Parquet write.

## Code
- `SAMPLES/sample1.py`: writes CSV to `temp/0517_data_lake.csv` and attempts Parquet with pyarrow.
- `SAMPLES/sample2.py`: reads CSV and prints row count.
- `SAMPLES/sample3.py`: logs data lake file existence to `temp/0517_data_lake_status.txt`.

## Output
- sample1: CSV created and parquet status printed.
- sample2: row count output.
- sample3: status file created.

## Explanation
- **Data Lake Integration**: local simulation of writing data lake assets.
- **Logic**: persist data as CSV and optionally Parquet if pyarrow installed.
- **Complexity**: O(n).
- **Use Case**: ETL pipelines for data warehousing.
- **Best Practice**: partition and compress; provide retries for failure.
