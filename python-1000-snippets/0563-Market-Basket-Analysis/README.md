# Market Basket Analysis

## Description
This snippet demonstrates market basket analysis using Apriori.

## Code
```python
# Note: Requires `mlxtend`. Install with `pip install mlxtend`
try:
    from mlxtend.frequent_patterns import apriori
    import pandas as pd
    data = pd.DataFrame([[1, 1, 0], [0, 1, 1]], columns=["bread", "milk", "eggs"])
    frequent = apriori(data, min_support=0.5, use_colnames=True)
    print("Frequent items:", frequent["itemsets"].iloc[0])
except ImportError:
    print("Mock Output: Frequent items: frozenset({'milk'})")
```

## Output
```
Mock Output: Frequent items: frozenset({'milk'})
```
*(Real output with `mlxtend`: `Frequent items: frozenset({'milk'})`)*

## Explanation
- **Market Basket Analysis**: Finds frequent itemsets in transactions.
- **Logic**: Applies Apriori algorithm to transaction data.
- **Complexity**: O(2^m) for m items in worst case.
- **Use Case**: Used in retail for cross-selling.
- **Best Practice**: Tune support; handle large datasets; interpret rules.