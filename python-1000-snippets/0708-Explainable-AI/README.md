# Explainable AI

## Description
This snippet demonstrates explainable AI for an e-commerce platform, using LIME to explain a fraud detection model’s predictions.

## Code
```python
# Explainable AI for fraud detection
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np

    # Fraud detection model
    class FraudModel:
        def __init__(self):
            # Initialize model weights
            self.weights = np.array([0.6, 0.4])  # Amount, frequency

        def predict_proba(self, features: np.ndarray) -> np.ndarray:
            # Predict fraud probability
            score = np.dot(features, self.weights)
            return np.array([1 / (1 + np.exp(-score)), 1 / (1 + np.exp(score))])

    # Simplified LIME explainer
    class LIMEExplainer:
        def __init__(self, model: FraudModel):
            # Initialize with model
            self.model = model

        def explain(self, features: np.ndarray) -> np.ndarray:
            # Generate local feature importance
            return np.abs(self.model.weights) * features / np.sum(np.abs(features))

    # Simulate explainable AI
    def explain_fraud_prediction(features: np.ndarray) -> np.ndarray:
        # Explain prediction
        model = FraudModel()
        explainer = LIMEExplainer(model)
        return explainer.explain(features)

    # Example usage
    features = np.array([1000, 5])  # Amount, frequency
    result = explain_fraud_prediction(features)
    print("Explainable AI:", result)
except ImportError:
    print("Mock Output: Explainable AI: [~0.6 ~0.002]")
```

## Output
```
Mock Output: Explainable AI: [~0.6 ~0.002]
```
*(Real output with `numpy`: `Explainable AI: [~0.6 ~0.002]`)*

## Explanation
- **Purpose**: Explainable AI provides human-understandable explanations for model predictions, enhancing trust.
- **Real-World Use Case**: In an e-commerce platform, LIME explains why a transaction is flagged as fraudulent, helping auditors understand model decisions.
- **Code Breakdown**:
  - The `FraudModel` class predicts fraud probabilities.
  - The `LIMEExplainer` class generates local feature importance.
  - The `explain_fraud_prediction` function simulates explanation.
- **Challenges**: Ensuring explanation fidelity, handling complex models, and scaling for real-time use.
- **Integration**: Works with Model Interpretability (Snippet 707) and AutoML Pipeline (Snippet 709) for transparent AI.
- **Complexity**: O(d) for d features.
- **Best Practices**: Use robust explainers, validate explanations, engage stakeholders, and test usability.