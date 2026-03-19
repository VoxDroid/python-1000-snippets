# sample3.py
# Detect anomalies using a OneClassSVM as a novelty detector.

import numpy as np
from sklearn.svm import OneClassSVM


def main() -> None:
    # Training data is roughly centered around 0.
    rng = np.random.RandomState(0)
    inliers = 0.3 * rng.randn(50, 2)
    outliers = rng.uniform(low=-6, high=6, size=(6, 2))

    model = OneClassSVM(kernel="rbf", gamma=0.1, nu=0.1)
    model.fit(inliers)

    test = np.vstack([inliers[:5], outliers])
    labels = model.predict(test)

    print("Test points (first 5 inliers, then outliers):")
    print(test)
    print("Labels (1=inlier, -1=outlier):", labels.tolist())


if __name__ == "__main__":
    main()
