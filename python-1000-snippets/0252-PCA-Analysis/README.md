# PCA Analysis

## Description
This snippet demonstrates Principal Component Analysis (PCA) using `scikit-learn` for dimensionality reduction and feature extraction.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — perform PCA and print explained variance ratios.
- `sample2.py` — reconstruct original data and compute reconstruction error.
- `sample3.py` — use PCA-transformed features in a downstream classifier.

Run any of them with:

```bash
python python-1000-snippets/0252-PCA-Analysis/SAMPLES/sample1.py
```

## Output
Each sample prints PCA statistics or performance metrics based on transformed features.

## Explanation
- **PCA**: Projects high-dimensional data into a lower-dimensional subspace that captures maximum variance.
- **Logic**: Fits PCA on synthetic data, transforms it, and optionally reconstructs or uses it for classification.
- **Use Case**: Useful for visualization, noise reduction, and speeding up downstream models.
- **Best Practice**: Standardize features before PCA, choose components based on cumulative variance, and evaluate downstream accuracy.
