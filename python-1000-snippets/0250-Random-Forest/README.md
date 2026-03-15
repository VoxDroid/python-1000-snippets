# Random Forest

## Description
This snippet demonstrates training and evaluating a random forest classifier using `scikit-learn`.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — train a random forest and print accuracy.
- `sample2.py` — examine feature importances and make sample predictions.
- `sample3.py` — train with out-of-bag (OOB) evaluation and print OOB score.

Run any of them with:

```bash
python python-1000-snippets/0250-Random-Forest/SAMPLES/sample1.py
```

## Output
Each sample prints accuracy, feature importance, or OOB score based on the trained model.

## Explanation
- **Random Forest**: Ensembles many decision trees for robustness.
- **Logic**: Trains on synthetic classification data and evaluates performance.
- **Best Practice**: Tune `n_estimators`, use `oob_score=True` for validation without a separate split.
