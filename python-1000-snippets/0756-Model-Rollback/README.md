# Model Rollback

## Description
This snippet demonstrates model rollback for an e-commerce platform, reverting to a previous recommendation model if the new model underperforms.

## Code
```python
# Model rollback for recommendations
# Note: Requires `numpy`, `sklearn`, `pickle`. Install with `pip install numpy scikit-learn`
try:
    import numpy as np
    from sklearn.linear_model import LogisticRegression
    import pickle
    import os

    # Recommendation model
    class RollbackModel:
        def __init__(self, model_path: str):
            # Load model or use default
            self.model = LogisticRegression()
            if os.path.exists(model_path):
                with open(model_path, 'rb') as f:
                    self.model = pickle.load(f)

        def predict(self, data: np.ndarray) -> np.ndarray:
            # Predict recommendations
            return self.model.predict_proba(data)[:, 1]

        def evaluate(self, data: np.ndarray, labels: np.ndarray) -> float:
            # Evaluate model performance
            return self.model.score(data, labels)

    # Simulate model rollback
    def rollback_recommendation(data: np.ndarray, labels: np.ndarray) -> np.ndarray:
        # Train new model, evaluate, and rollback if needed
        new_model = LogisticRegression()
        new_model.fit(data, labels)
        with open("new_model.pkl", "wb") as f:
            pickle.dump(new_model, f)
        new_deployed = RollbackModel("new_model.pkl")
        old_deployed = RollbackModel("old_model.pkl")
        new_score = new_deployed.evaluate(data, labels)
        old_score = old_deployed.evaluate(data, labels)
        return new_deployed.predict(data) if new_score >= old_score else old_deployed.predict(data)

    # Example usage
    data = np.random.randn(10, 5)  # Customer features
    labels = np.random.randint(0, 2, 10)  # Preferences
    old_model = LogisticRegression().fit(data, labels)
    with open("old_model.pkl", "wb") as f:
        pickle.dump(old_model, f)
    result = rollback_recommendation(data, labels)
    print("Model rollback result:", result)
except ImportError:
    print("Mock Output: Model rollback result: [~0.5, ~0.3, ~0.6, ...]")
```

## Output
```
Mock Output: Model rollback result: [~0.5, ~0.3, ~0.6, ...]
```
*(Real output with `numpy`, `sklearn`: `Model rollback result: [<10 probabilities>]`)*

## Explanation
- **Purpose**: Model rollback reverts to a previous model if a new model fails performance criteria, ensuring reliability.
- **Real-World Use Case**: In an e-commerce platform, a new recommendation model is rolled back if it reduces engagement compared to the old model.
- **Code Breakdown**:
  - The `RollbackModel` class loads and evaluates models.
  - The `rollback_recommendation` function compares new and old model performance.
  - The example simulates rollback based on accuracy.
- **Challenges**: Defining rollback criteria, managing model versions, ensuring quick reversion, and monitoring impacts.
- **Integration**: Works with Model Versioning (Snippet 743) and Canary Deployment (Snippet 754) for safe updates.
- **Complexity**: O(n*d) for n samples and d features per evaluation.
- **Best Practices**: Define clear metrics, automate rollback, version models, and test reversion.
- **Extensions**: Integrate with monitoring tools or automate rollback in CI/CD pipelines.