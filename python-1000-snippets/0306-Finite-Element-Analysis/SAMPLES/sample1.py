#!/usr/bin/env python3
"""1D bar finite element analysis with fixed boundary conditions."""

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


def apply_boundary_conditions(K, F, fixed_indices):
    # Remove fixed DOFs by eliminating corresponding rows/columns
    free = [i for i in range(K.shape[0]) if i not in fixed_indices]
    Kf = K[np.ix_(free, free)]
    Ff = F[free]
    return Kf, Ff, free


def main():
    n_nodes = 4
    E = 210e9  # Young's modulus (Pa)
    A = 0.01  # Cross-sectional area (m^2)
    L = 3.0  # Length (m)

    K = assemble_bar_stiffness(n_nodes, E, A, L)
    F = np.zeros(n_nodes)
    F[-1] = 1000.0  # Force at right end (N)

    Kf, Ff, free = apply_boundary_conditions(K, F, fixed_indices=[0])
    Uf = np.linalg.solve(Kf, Ff)

    U = np.zeros(n_nodes)
    U[free] = Uf
    print("Displacements:", U)


if __name__ == '__main__':
    main()
