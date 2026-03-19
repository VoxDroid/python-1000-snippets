# sample2.py
# Compute linkage matrix and print merge distances using scipy.

import numpy as np
from scipy.cluster.hierarchy import linkage
from sklearn.datasets import load_iris


def main() -> None:
    data = load_iris(as_frame=True)
    X = data.data

    # Use ward linkage for hierarchical clustering
    Z = linkage(X, method="ward")

    # Print the first few merge steps
    print("First 5 linkage steps (idx1, idx2, dist, sample_count):")
    for row in Z[:5]:
        print(row)

    print("Total merges:", Z.shape[0])


if __name__ == "__main__":
    main()
