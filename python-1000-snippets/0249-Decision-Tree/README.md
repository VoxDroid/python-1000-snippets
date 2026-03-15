# Decision Tree

## Description
This snippet demonstrates training and inspecting a decision tree classifier using `scikit-learn`.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — train a decision tree, print test accuracy, and report tree depth.
- `sample2.py` — show feature importances and make a sample prediction.
- `sample3.py` — export the learned tree structure as readable text.

Run any of them with:

```bash
python python-1000-snippets/0249-Decision-Tree/SAMPLES/sample1.py
```

## Output
Each sample prints metrics and/or the decision logic extracted from the trained tree.

## Explanation
- **Decision Tree**: Splits data recursively using feature thresholds.
- **Logic**: Trains on synthetic classification data and inspects the resulting tree.
- **Best Practice**: Limit depth to avoid overfitting; interpret feature importance.
