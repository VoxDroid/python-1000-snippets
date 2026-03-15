# sample2.py
# Train a decision tree and display feature importances.

from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier


def main():
    X, y = make_classification(n_samples=200, n_features=4, n_informative=2, n_redundant=0, random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)

    print('Feature importances:', [float(v) for v in model.feature_importances_])
    print('Sample prediction:', model.predict([X[0]]).tolist())


if __name__ == '__main__':
    main()
