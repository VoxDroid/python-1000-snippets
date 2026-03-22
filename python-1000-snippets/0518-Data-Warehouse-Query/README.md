# Data Warehouse Query

## Description
This snippet demonstrates data warehouse query patterns using SQLite in pure Python.

## Code
- `SAMPLES/sample1.py`: creates an in-memory table and computes total sales.
- `SAMPLES/sample2.py`: filters rows via SQL query.
- `SAMPLES/sample3.py`: writes query summary to `temp/0518_warehouse_summary.txt`.

## Output
- sample1: `Total sales: 600`
- sample2: `Filtered quantities >5: [10, 30]`
- sample3: summary file content.

## Explanation
- **Data Warehouse Query**: run SQL aggregation on table data.
- **Logic**: use SQLite to simulate warehouse query execution.
- **Complexity**: O(n) for row scans.
- **Use Case**: analytics queries and ETL validation scripts.
- **Best Practice**: index key columns, and use bulk operations for large data.
