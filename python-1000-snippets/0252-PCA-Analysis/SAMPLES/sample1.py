# sample1.py
# Perform PCA on synthetic data and print explained variance ratio.

from sklearn.decomposition import PCA
from sklearn.datasets import make_classification


def main():
    X, _ = make_classification(n_samples=150, n_features=5, n_informative=3, n_redundant=0, random_state=42)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    print("Explained variance ratio:", pca.explained_variance_ratio_.tolist())
    print("Transformed shape:", X_pca.shape)


if __name__ == "__main__":
    main()
