# 0246 - Machine Learning Model Cheatsheet

- Use `scikit-learn` for classical ML (Logistic Regression, Random Forest, etc.)
- Persist models with `joblib.dump` / `joblib.load` for reuse.
- Use `Pipeline` to chain preprocessing (`StandardScaler`) + model.
- Always split data: `train_test_split(X, y, test_size=0.2)`.
