# 0454-Deep-Learning-Pipeline Cheatsheet

- Use `sklearn.neural_network.MLPClassifier` for simple neural network models.
- Wrap preprocessing (e.g., `StandardScaler`) and the model in a `Pipeline` for clean workflows.
- Persist models with `joblib.dump` / `joblib.load`.

Example:
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

pipe = Pipeline([("scaler", StandardScaler()), ("mlp", MLPClassifier())])
pipe.fit(X, y)
```
