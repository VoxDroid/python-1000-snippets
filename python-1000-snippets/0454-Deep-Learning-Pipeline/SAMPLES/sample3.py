# sample3.py
# Show how to inspect the weights of a trained MLP classifier.

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler


def main() -> None:
    data = load_digits(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    clf = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=500, random_state=0)
    clf.fit(X_train_scaled, y_train)

    print("Test accuracy:", clf.score(scaler.transform(X_test), y_test))
    print("Number of layers:", len(clf.coefs_))
    print("Shapes of weight matrices:")
    for i, coef in enumerate(clf.coefs_):
        print(f"  layer {i}: {coef.shape}")


if __name__ == "__main__":
    main()
