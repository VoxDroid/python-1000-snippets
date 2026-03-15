# sample1.py
# Train a simple neural network (MLP) on synthetic classification data.

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


def main():
    X, y = make_classification(n_samples=200, n_features=4, n_informative=3, n_redundant=0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    model = MLPClassifier(hidden_layer_sizes=(20, 10), max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    print("Test accuracy:", model.score(X_test, y_test))


if __name__ == "__main__":
    main()
