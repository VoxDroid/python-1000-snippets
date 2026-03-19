# sample1.py
# Demonstrate imputing missing values in a dataset.

import numpy as np
from sklearn.impute import SimpleImputer


def main() -> None:
    # Synthetic dataset with missing values
    X = np.array(
        [
            [1.0, 2.0, np.nan],
            [2.0, np.nan, 6.0],
            [np.nan, 3.0, 9.0],
            [4.0, 5.0, 12.0],
        ]
    )

    imputer = SimpleImputer(strategy="mean")
    X_imputed = imputer.fit_transform(X)

    print("Original data:")
    print(X)
    print("\nImputed data (mean strategy):")
    print(X_imputed)


if __name__ == "__main__":
    main()
