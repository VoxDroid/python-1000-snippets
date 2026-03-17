#!/usr/bin/env python3
"""2D truss analysis for a triangular element."""

import numpy as np


def truss_stiffness_matrix(nodes, elements, E, A):
    # nodes: list of (x, y)
    # elements: list of (i, j)
    ndof = 2 * len(nodes)
    K = np.zeros((ndof, ndof), dtype=float)

    for i, j in elements:
        x1, y1 = nodes[i]
        x2, y2 = nodes[j]
        L = np.hypot(x2 - x1, y2 - y1)
        c = (x2 - x1) / L
        s = (y2 - y1) / L
        k_local = (E * A / L) * np.array(
            [[ c*c,  c*s, -c*c, -c*s],
             [ c*s,  s*s, -c*s, -s*s],
             [-c*c, -c*s,  c*c,  c*s],
             [-c*s, -s*s,  c*s,  s*s]],
            dtype=float,
        )

        dof = [2 * i, 2 * i + 1, 2 * j, 2 * j + 1]
        for a in range(4):
            for b in range(4):
                K[dof[a], dof[b]] += k_local[a, b]

    return K


def apply_boundary_conditions(K, F, fixed_dof):
    free = [i for i in range(K.shape[0]) if i not in fixed_dof]
    Kf = K[np.ix_(free, free)]
    Ff = F[free]
    return Kf, Ff, free


def main():
    # Triangular truss: nodes A, B, C
    nodes = [(0.0, 0.0), (1.0, 0.0), (0.5, 0.866)]
    elements = [(0, 2), (1, 2), (0, 1)]

    E = 210e9
    A = 0.005

    K = truss_stiffness_matrix(nodes, elements, E, A)

    # Apply a downward load at node C (index 2)
    F = np.zeros(2 * len(nodes), dtype=float)
    F[2 * 2 + 1] = -1000.0

    # Fix nodes A and B (both DOFs)
    fixed = [0, 1, 2, 3]
    Kf, Ff, free = apply_boundary_conditions(K, F, fixed)

    Uf = np.linalg.solve(Kf, Ff)
    U = np.zeros(2 * len(nodes), dtype=float)
    U[free] = Uf

    print("Truss displacements:", np.round(U, 4))


if __name__ == '__main__':
    main()
