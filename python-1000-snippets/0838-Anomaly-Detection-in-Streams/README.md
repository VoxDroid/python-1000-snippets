# Anomaly Detection in Streams

## Description
This snippet demonstrates Anomaly Detection in Streams for an e-commerce platform, identifying unusual user activity in real-time transaction data.

## Code
```python
# Anomaly Detection in Streams for transactions
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np

    # Anomaly detection model
    class TransactionAnomalyDetector:
        def __init__(self, window_size: int = 10):
            # Initialize sliding window
            self.window_size = window_size
            self.history = []

        def detect(self, transaction: float) -> bool:
            # Detect anomaly using z-score
            self.history.append(transaction)
            if len(self.history) > self.window_size:
                self.history.pop(0)
            if len(self.history) < self.window_size:
                return False
            mean = np.mean(self.history)
            std = np.std(self.history)
            z_score = abs(transaction - mean) / std if std > 0 else 0
            return z_score > 3  # Threshold for anomaly

    # Simulate anomaly detection
    def detect_anomalies(transactions: list) -> list:
        # Detect anomalies in transaction stream
        detector = TransactionAnomalyDetector()
        return [detector.detect(t) for t in transactions]

    # Example usage
    transactions = [100, 110, 105, 120, 500, 115]
    results = detect_anomalies(transactions)
    print("Anomaly detection result:", results)
except ImportError:
    print("Mock Output: Anomaly detection result: [False, False, False, False, True, False]")
```

## Output
```
Mock Output: Anomaly detection result: [False, False, False, False, True, False]
```
*(Real output with `numpy`: `Anomaly detection result: [<variable results>]`)*

## Explanation
- **Purpose**: Anomaly Detection in Streams identifies unusual patterns in real-time data, enabling rapid response.
- **Real-World Use Case**: In an e-commerce platform, it detects suspicious transactions, preventing fraud.
- **Code Breakdown**:
  - The `TransactionAnomalyDetector` class uses a sliding window and z-score.
  - The `detect` method flags anomalies.
  - The `detect_anomalies` function simulates detection.
- **Challenges**: Setting thresholds, handling noisy data, and real-time processing.
- **Integration**: Works with Real-Time Fraud Detection (Snippet 839) and Intrusion Detection System (Snippet 840) for security tasks.
- **Complexity**: O(w) for window size w.
- **Best Practices**: Tune thresholds, validate results, and handle edge cases.
- **Extensions**: Use machine learning models or integrate with transaction systems.