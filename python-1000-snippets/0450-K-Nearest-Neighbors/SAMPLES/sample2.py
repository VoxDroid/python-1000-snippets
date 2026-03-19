# sample2.py
# Demonstrate K-Nearest Neighbors regression on synthetic data.

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error


def main() -> None:
    rng = np.random.default_rng(0)
    X = rng.uniform(-3, 3, size=(200, 1))
    y = np.sin(X).ravel() + rng.normal(scale=0.1, size=X.shape[0])

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    reg = KNeighborsRegressor(n_neighbors=5)
    reg.fit(X_train, y_train)

    preds = reg.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    print("Test MSE:", mse)
    print("Sample predictions:", preds[:5])


if __name__ == "__main__":
    main()
