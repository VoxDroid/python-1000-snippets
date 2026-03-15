# sample2.py
# Train a random forest classifier and show feature importances and predictions.

from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def main():
    X, y = make_classification(n_samples=200, n_features=5, n_informative=3, n_redundant=0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)

    print('Feature importances:', [float(v) for v in model.feature_importances_])
    sample = X_test[:3]
    print('Sample inputs:', sample.tolist())
    print('Predicted labels:', model.predict(sample).tolist())


if __name__ == '__main__':
    main()
