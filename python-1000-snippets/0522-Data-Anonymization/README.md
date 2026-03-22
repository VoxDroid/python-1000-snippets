# Data Anonymization

## Description
This snippet demonstrates data anonymization techniques with simple heuristics and outputs.

## Code
- `SAMPLES/sample1.py`: random mapping for names to pseudonyms.
- `SAMPLES/sample2.py`: deterministic scrub of PII fields.
- `SAMPLES/sample3.py`: write anonymized rows to `temp/0522_anonymized.txt`.

## Output
- sample1: anonymized names list.
- sample2: anonymized records with standard masked fields.
- sample3: file output at `temp/0522_anonymized.txt`.

## Explanation
- **Data Anonymization**: hide personally identifiable data in records.
- **Logic**: substitute values with placeholders or random pseudonyms.
- **Complexity**: O(n).
- **Use Case**: data privacy in analytics and testing.
- **Best Practice**: keep mapping consistent where needed; avoid data leaks; validate coverage.
