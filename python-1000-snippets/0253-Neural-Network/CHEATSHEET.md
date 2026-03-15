# 0253 - Neural Network Cheatsheet

## Quick Start
```bash
pip install scikit-learn
python python-1000-snippets/0253-Neural-Network/SAMPLES/sample1.py
```

## Key Concepts
- Use `MLPClassifier(hidden_layer_sizes=(...))` for multi-layer perceptrons.
- Use `model.predict_proba(X)` to get class probability estimates.
- Save models with `joblib.dump(model, path)` and load with `joblib.load(path)`.

## Tips
- Increase `max_iter` if you see `ConvergenceWarning`.
- Scale your features (`StandardScaler`) for faster convergence.
- Use `random_state` for reproducible results.
