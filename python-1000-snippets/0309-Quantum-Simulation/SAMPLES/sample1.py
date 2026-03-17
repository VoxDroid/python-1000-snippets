#!/usr/bin/env python3
"""Single-qubit Hadamard gate simulation."""

import numpy as np


def hadamard():
    return np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)


def measure_probabilities(state):
    probs = np.abs(state) ** 2
    return {"0": float(probs[0]), "1": float(probs[1])}


def main():
    # Start in |0> state
    state = np.array([1.0, 0.0], dtype=complex)
    state = hadamard() @ state

    probs = measure_probabilities(state)
    print("Probabilities:", {k: round(v, 2) for k, v in probs.items()})


if __name__ == '__main__':
    main()
