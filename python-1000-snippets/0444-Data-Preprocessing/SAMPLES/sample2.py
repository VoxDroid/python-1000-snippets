# sample2.py
# Demonstrate feature scaling with StandardScaler and MinMaxScaler.

import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def main() -> None:
    X = np.array([[1.0, 10.0], [2.0, 20.0], [3.0, 30.0], [4.0, 40.0]])

    scaler = StandardScaler()
    scaled = scaler.fit_transform(X)

    minmax = MinMaxScaler()
    scaled_minmax = minmax.fit_transform(X)

    print("Original:")
    print(X)
    print("\nStandard scaled:")
    print(scaled)
    print("\nMin-max scaled:")
    print(scaled_minmax)


if __name__ == "__main__":
    main()
