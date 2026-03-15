# Machine Learning Model

## Description
This snippet demonstrates a simple machine learning workflow using `scikit-learn`.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — train a logistic regression model and evaluate test accuracy.
- `sample2.py` — persist a trained model using `joblib`, then reload it and compare results.
- `sample3.py` — build a pipeline with scaling + logistic regression and evaluate it.

Run any of them with:

```bash
python python-1000-snippets/0246-Machine-Learning-Model/SAMPLES/sample1.py
```

## Output
Each sample prints model accuracy or related metrics when run.

## Explanation
- **Machine Learning Workflow**: Uses synthetic data and `scikit-learn` to train/evaluate models.
- **Logic**: Demonstrates training, saving/loading, preprocessing, and evaluation.
- **Best Practice**: Use train/test splits, persist models, and normalize data before training.
