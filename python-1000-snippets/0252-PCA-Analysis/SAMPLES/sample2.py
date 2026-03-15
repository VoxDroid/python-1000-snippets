# sample2.py
# Reconstruct data from PCA and compute reconstruction error.

from sklearn.decomposition import PCA
from sklearn.datasets import make_classification
import numpy as np


def main():
    X, _ = make_classification(n_samples=150, n_features=5, n_informative=3, n_redundant=0, random_state=42)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    X_reconstructed = pca.inverse_transform(X_pca)

    mse = np.mean((X - X_reconstructed) ** 2)
    print("Reconstruction MSE:", float(mse))


if __name__ == "__main__":
    main()
