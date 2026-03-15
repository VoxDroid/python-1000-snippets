# sample2.py
# Show predicted class probabilities for sample inputs using an MLP classifier.

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


def main():
    X, y = make_classification(n_samples=200, n_features=4, n_informative=3, n_redundant=0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    model = MLPClassifier(hidden_layer_sizes=(20, 10), max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    samples = X_test[:5]
    probs = model.predict_proba(samples)

    print('Sample inputs:', samples.tolist())
    print('Predicted probabilities:')
    for p in probs:
        print([float(x) for x in p])


if __name__ == "__main__":
    main()
