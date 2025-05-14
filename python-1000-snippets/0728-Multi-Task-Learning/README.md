# Multi-Task Learning

## Description
This snippet demonstrates multi-task learning for an e-commerce platform, training a model to predict both product preferences and churn risk simultaneously.

## Code
```python
# Multi-task learning for preferences and churn
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np

    # Multi-task learning model
    class MultiTaskModel:
        def __init__(self):
            # Initialize shared and task-specific weights
            self.shared_weights = np.random.randn(5, 3)
            self.pref_weights = np.random.randn(3, 2)
            self.churn_weights = np.random.randn(3, 1)

        def train(self, data: np.ndarray, pref_labels: np.ndarray, churn_labels: np.ndarray) -> None:
            shared = data @ self.shared_weights
            pref_pred = shared @ self.pref_weights
            churn_pred = shared @ self.churn_weights

            pref_grad = shared.T @ (pref_pred - pref_labels)  # (3, 2)
            churn_grad = shared.T @ (churn_pred - churn_labels)  # (3, 1)

            self.pref_weights -= 0.1 * pref_grad
            self.churn_weights -= 0.1 * churn_grad

            shared_error = (pref_pred - pref_labels) @ self.pref_weights.T + \
                        (churn_pred - churn_labels) @ self.churn_weights.T  # (5, 3)

            self.shared_weights -= 0.1 * data.T @ shared_error  # (5, 5) @ (5, 3) = (5, 3)

        def predict(self, data: np.ndarray) -> tuple:
            # Predict preferences and churn
            shared = data @ self.shared_weights
            return shared @ self.pref_weights, shared @ self.churn_weights

    # Simulate multi-task learning
    def train_multi_task(data: np.ndarray, pref_labels: np.ndarray, churn_labels: np.ndarray) -> tuple:
        # Train and predict for both tasks
        model = MultiTaskModel()
        model.train(data, pref_labels, churn_labels)
        return model.predict(data)

    # Example usage
    data = np.random.randn(5, 5)
    pref_labels = np.random.randn(5, 2)
    churn_labels = np.random.randn(5, 1)
    pref_result, churn_result = train_multi_task(data, pref_labels, churn_labels)
    print("Multi-task learning result (preferences, churn):", pref_result, churn_result)
except ImportError:
    print("Mock Output: Multi-task learning result (preferences, churn): [[~0.0, ~0.0], ...], [[~0.0], ...]")
```

## Output
```
Mock Output: Multi-task learning result (preferences, churn): [[~0.0, ~0.0], ...], [[~0.0], ...]
```
*(Real output with `numpy`: `Multi-task learning result (preferences, churn): [<5x2 floats>, <5x1 floats>]`)*

## Explanation
- **Purpose**: Multi-task learning trains a model on multiple related tasks, improving efficiency and generalization.
- **Real-World Use Case**: In an e-commerce platform, multi-task learning predicts user product preferences and churn risk, leveraging shared patterns.
- **Code Breakdown**:
  - The `MultiTaskModel` class uses shared and task-specific weights.
  - The `train` method updates weights for both tasks.
  - The `train_multi_task` function simulates multi-task training.
- **Challenges**: Balancing task losses, handling task conflicts, and ensuring shared feature quality.
- **Integration**: Works with Curriculum Learning (Snippet 727) and Multi-Modal Learning (Snippet 729) for complex tasks.
- **Complexity**: O(n*d) for n samples and d dimensions.
- **Best Practices**: Balance task weights, validate predictions, tune architectures, and test generalization.