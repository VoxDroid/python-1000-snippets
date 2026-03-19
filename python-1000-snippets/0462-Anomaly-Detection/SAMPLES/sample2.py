# sample2.py
# Detect anomalies using LocalOutlierFactor for unsupervised outlier detection.

import numpy as np
from sklearn.neighbors import LocalOutlierFactor


def main() -> None:
    data = np.array([[0.5], [0.2], [0.2], [0.4], [0.3], [10.0]])
    lof = LocalOutlierFactor(n_neighbors=2, contamination=0.2)
    labels = lof.fit_predict(data)

    print("Data:", data.ravel().tolist())
    print("LOF labels (-1 anomaly, 1 inlier):", labels.tolist())


if __name__ == "__main__":
    main()
