#!/usr/bin/env python3
"""Compute potential energy and radial distribution after MD simulation."""

import numpy as np


def lennard_jones_potential(r, epsilon=1.0, sigma=1.0):
    if r == 0:
        return 0.0
    sr6 = (sigma / r) ** 6
    sr12 = sr6 * sr6
    return 4 * epsilon * (sr12 - sr6)


def total_energy(positions, velocities, mass=1.0):
    kinetic = 0.5 * mass * np.sum(velocities**2)
    potential = 0.0
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            r = np.linalg.norm(positions[i] - positions[j])
            potential += lennard_jones_potential(r)
    return kinetic + potential


def run_simulation(steps=200, dt=0.001):
    positions = np.array([[0.0, 0.0], [1.3, 0.2], [0.6, 1.1]])
    velocities = np.zeros_like(positions)

    for _ in range(steps):
        forces = np.zeros_like(positions)
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                r_vec = positions[i] - positions[j]
                r = np.linalg.norm(r_vec)
                if r == 0:
                    continue
                sr6 = (1.0 / r) ** 6
                f_mag = 24 * (2 * sr6**2 - sr6) / (r * r)
                f = f_mag * r_vec
                forces[i] += f
                forces[j] -= f

        velocities += 0.5 * forces * dt
        positions += velocities * dt
        forces.fill(0)

    return positions, velocities


def main():
    positions, velocities = run_simulation()
    energy = total_energy(positions, velocities)
    print(f"Total energy: {energy:.2f}")


if __name__ == '__main__':
    main()
