# sample2.py
# Compare different SVM kernels and their validation scores.

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    for kernel in ["linear", "rbf", "poly"]:
        clf = SVC(kernel=kernel, gamma="scale")
        scores = cross_val_score(clf, X, y, cv=5)
        print(f"Kernel={kernel}: mean accuracy={scores.mean():.3f}")


if __name__ == "__main__":
    main()
