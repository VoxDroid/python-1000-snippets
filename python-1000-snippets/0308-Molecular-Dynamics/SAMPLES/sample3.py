#!/usr/bin/env python3
"""Molecular dynamics with a simple thermostat (velocity scaling)."""

import numpy as np


def velocity_verlet(positions, velocities, forces, mass, dt):
    velocities += 0.5 * (forces / mass) * dt
    positions += velocities * dt
    return positions, velocities


def compute_forces(positions, epsilon=1.0, sigma=1.0):
    forces = np.zeros_like(positions)
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            r_vec = positions[i] - positions[j]
            r = np.linalg.norm(r_vec)
            if r == 0:
                continue
            sr6 = (sigma / r) ** 6
            f_mag = 24 * epsilon * (2 * sr6**2 - sr6) / (r * r)
            forces[i] += f_mag * r_vec
            forces[j] -= f_mag * r_vec
    return forces


def kinetic_energy(velocities, mass=1.0):
    return 0.5 * mass * np.sum(velocities**2)


def apply_thermostat(velocities, target_temp):
    current_ke = kinetic_energy(velocities)
    if current_ke == 0:
        return velocities
    scale = np.sqrt(target_temp / current_ke)
    return velocities * scale


def main():
    positions = np.array([[0.0, 0.0], [1.2, 0.0], [0.6, 1.1]])
    velocities = np.random.normal(0, 0.1, positions.shape)
    mass = 1.0
    dt = 0.001
    target_ke = 0.1

    for _ in range(200):
        forces = compute_forces(positions)
        positions, velocities = velocity_verlet(positions, velocities, forces, mass, dt)
        forces = compute_forces(positions)
        velocities += 0.5 * (forces / mass) * dt
        velocities = apply_thermostat(velocities, target_ke)

    avg_ke = kinetic_energy(velocities)
    print(f"Average kinetic energy: {avg_ke:.2f}")


if __name__ == '__main__':
    main()
