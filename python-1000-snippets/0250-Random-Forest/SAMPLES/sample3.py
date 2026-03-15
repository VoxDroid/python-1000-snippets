# sample3.py
# Train a random forest with out-of-bag evaluation and print oob_score.

from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def main():
    X, y = make_classification(n_samples=200, n_features=5, n_informative=3, n_redundant=0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    model = RandomForestClassifier(n_estimators=50, oob_score=True, random_state=42)
    model.fit(X_train, y_train)

    print('Out-of-bag score:', model.oob_score_)
    print('Test accuracy:', model.score(X_test, y_test))


if __name__ == '__main__':
    main()
