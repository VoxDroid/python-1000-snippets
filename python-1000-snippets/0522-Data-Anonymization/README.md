# Data Anonymization

## Description
This snippet demonstrates anonymizing data using `faker`.

## Code
```python
# Note: Requires `faker` and `pandas`. Install with `pip install faker pandas`
try:
    from faker import Faker
    import pandas as pd
    fake = Faker()
    data = pd.DataFrame({"name": ["Alice", "Bob"]})
    data["name"] = [fake.name() for _ in range(len(data))]
    print("Anonymized names:", data["name"].tolist()[:2])
except ImportError:
    print("Mock Output: Anonymized names: ['John Doe', 'Jane Smith']")
```

## Output
```
Mock Output: Anonymized names: ['John Doe', 'Jane Smith']
```
*(Real output with `faker`: `Anonymized names: [<random names>]`)*

## Explanation
- **Data Anonymization**: Replaces names with fake ones.
- **Logic**: Uses `faker` to generate random names.
- **Complexity**: O(n) for n rows.
- **Use Case**: Used for privacy protection in datasets.
- **Best Practice**: Preserve data structure; test anonymization; comply with regulations.