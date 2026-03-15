# sample3.py
# Export a trained decision tree as human-readable text.

from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, export_text


def main():
    X, y = make_classification(n_samples=200, n_features=2, n_informative=2, n_redundant=0, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)

    tree_text = export_text(model, feature_names=[f"f{i}" for i in range(X.shape[1])])
    print(tree_text)


if __name__ == '__main__':
    main()
