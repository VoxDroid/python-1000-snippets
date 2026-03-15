# sample3.py
# Show how PCA components can be used as features for a simple classifier.

from sklearn.decomposition import PCA
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def main():
    X, y = make_classification(n_samples=200, n_features=5, n_informative=3, n_redundant=0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    pca = PCA(n_components=2)
    X_train_pca = pca.fit_transform(X_train)
    X_test_pca = pca.transform(X_test)

    model = LogisticRegression(max_iter=500)
    model.fit(X_train_pca, y_train)

    print("Test accuracy on PCA features:", model.score(X_test_pca, y_test))


if __name__ == "__main__":
    main()
