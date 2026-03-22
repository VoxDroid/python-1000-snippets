# Schema Evolution

## Description
This snippet demonstrates schema evolution handling using pure Python structures.

## Code
- `SAMPLES/sample1.py`: merges rows with evolving schema and outputs key columns.
- `SAMPLES/sample2.py`: gives new field defaults to old rows.
- `SAMPLES/sample3.py`: writes schema fields to `temp/0521_schema_fields.txt`.

## Output
- sample1: `Schema evolved: ['col1', 'col2']` and merged rows.
- sample2: `Evolved rows: ...` with default col2.
- sample3: writes schema fields file.

## Explanation
- **Schema Evolution**: adapts rows to new schema with backward compatibility.
- **Logic**: build unified keyset across row variants.
- **Complexity**: O(n) across row count.
- **Use Case**: data migration and evolving events during ingestion.
- **Best Practice**: keep schema versioning, check required fields, and provide defaults.
