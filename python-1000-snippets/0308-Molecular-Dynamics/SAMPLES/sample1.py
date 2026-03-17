#!/usr/bin/env python3
"""3-particle Lennard-Jones molecular dynamics simulation."""

import numpy as np


def lennard_jones_force(r_vec, epsilon=1.0, sigma=1.0):
    r = np.linalg.norm(r_vec)
    if r == 0:
        return np.zeros_like(r_vec)
    sr6 = (sigma / r) ** 6
    sr12 = sr6 * sr6
    magnitude = 24 * epsilon * (2 * sr12 - sr6) / (r * r)
    return magnitude * r_vec


def run_simulation(steps=200, dt=0.001):
    # start with 3 particles in a triangle
    positions = np.array([[0.0, 0.0], [1.2, 0.0], [0.6, 1.0]])
    velocities = np.zeros_like(positions)
    mass = 1.0

    for _ in range(steps):
        forces = np.zeros_like(positions)
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                f = lennard_jones_force(positions[i] - positions[j])
                forces[i] += f
                forces[j] -= f

        # velocity Verlet integration
        velocities += 0.5 * (forces / mass) * dt
        positions += velocities * dt

        # recompute forces for new positions
        forces.fill(0)
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                f = lennard_jones_force(positions[i] - positions[j])
                forces[i] += f
                forces[j] -= f

        velocities += 0.5 * (forces / mass) * dt

    return positions, velocities


def main():
    positions, velocities = run_simulation()
    print("Particle positions:")
    print(np.round(positions, 2))


if __name__ == '__main__':
    main()
