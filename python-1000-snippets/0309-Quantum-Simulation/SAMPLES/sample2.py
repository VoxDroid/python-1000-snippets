#!/usr/bin/env python3
"""Two-qubit Bell state simulation (Hadamard + CNOT)."""

import numpy as np


def kron(*matrices):
    result = matrices[0]
    for m in matrices[1:]:
        result = np.kron(result, m)
    return result


def hadamard():
    return np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)


def cnot():
    return np.array(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]],
        dtype=complex,
    )


def measure_probabilities(state):
    probs = np.abs(state) ** 2
    basis = ["00", "01", "10", "11"]
    return {basis[i]: float(probs[i]) for i in range(4)}


def main():
    # Start in |00>
    state = np.zeros(4, dtype=complex)
    state[0] = 1.0

    # Apply H on qubit 0
    H0 = kron(hadamard(), np.eye(2, dtype=complex))
    state = H0 @ state

    # Apply CNOT
    state = cnot() @ state

    probs = measure_probabilities(state)
    # Round probabilities for readability
    probs = {k: round(v, 2) for k, v in probs.items()}
    print("Bell state probabilities:", probs)


if __name__ == '__main__':
    main()
