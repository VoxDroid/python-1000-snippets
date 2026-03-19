# 0455-Transfer-Learning Cheatsheet

- Transfer learning commonly starts with a pre-trained model and adapts it to a new but related task.
- In scikit-learn, you can simulate transfer learning by saving/loading models with `joblib` and then continuing training.

Example:
```python
import joblib
model = joblib.load('model.joblib')
model.fit(X_new, y_new)
joblib.dump(model, 'model_finetuned.joblib')
```
