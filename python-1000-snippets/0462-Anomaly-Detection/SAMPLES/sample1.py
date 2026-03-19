# sample1.py
# Detect anomalies using IsolationForest on a small numeric dataset.

import numpy as np
from sklearn.ensemble import IsolationForest


def main() -> None:
    data = np.array([[1], [2], [2], [3], [3], [4], [100]])
    model = IsolationForest(contamination=0.15, random_state=0)
    labels = model.fit_predict(data)

    # -1 indicates anomaly, 1 indicates inlier
    print("Data:", data.ravel().tolist())
    print("Anomaly labels:", labels.tolist())


if __name__ == "__main__":
    main()
