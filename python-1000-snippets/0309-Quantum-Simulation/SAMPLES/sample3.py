#!/usr/bin/env python3
"""Time evolution of a two-level quantum system under a simple Hamiltonian."""

import numpy as np


def pauli_x():
    return np.array([[0, 1], [1, 0]], dtype=complex)


def unitary_from_hamiltonian(H, dt):
    # For 2x2 Hermitian H, we can compute exp(-i H dt) analytically via eigen-decomposition
    eigvals, eigvecs = np.linalg.eigh(H)
    U = eigvecs @ np.diag(np.exp(-1j * eigvals * dt)) @ eigvecs.conj().T
    return U


def main():
    omega = 2.0
    H = 0.5 * omega * pauli_x()
    dt = 0.1
    steps = 50

    # Start in |0> state
    state = np.array([1.0, 0.0], dtype=complex)

    for _ in range(steps):
        U = unitary_from_hamiltonian(H, dt)
        state = U @ state

    print("Final state amplitudes:", np.round(state, 2))


if __name__ == '__main__':
    main()
