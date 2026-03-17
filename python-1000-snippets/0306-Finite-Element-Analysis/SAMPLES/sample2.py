#!/usr/bin/env python3
"""Compute natural frequencies for a 1D bar using eigenanalysis."""

import numpy as np


def assemble_bar_stiffness(n_nodes, E, A, length):
    element_length = length / (n_nodes - 1)
    k = E * A / element_length
    K = np.zeros((n_nodes, n_nodes), dtype=float)
    for i in range(n_nodes - 1):
        K[i, i] += k
        K[i, i + 1] -= k
        K[i + 1, i] -= k
        K[i + 1, i + 1] += k
    return K


def assemble_mass_matrix(n_nodes, mass_per_length, length):
    total_mass = mass_per_length * length
    m = total_mass / n_nodes
    return np.eye(n_nodes, dtype=float) * m


def main():
    n_nodes = 10
    E = 210e9
    A = 0.01
    L = 5.0
    mass_per_length = 0.5

    K = assemble_bar_stiffness(n_nodes, E, A, L)
    M = assemble_mass_matrix(n_nodes, mass_per_length, L)

    # Fix both ends (remove first and last DOF)
    free = list(range(1, n_nodes - 1))
    Kf = K[np.ix_(free, free)]
    Mf = M[np.ix_(free, free)]

    eigvals, _ = np.linalg.eig(np.linalg.inv(Mf).dot(Kf))
    omegas = np.sqrt(np.abs(eigvals))
    omegas.sort()

    print("Natural frequencies (rad/s):", np.round(omegas[:3], 2))


if __name__ == '__main__':
    main()
