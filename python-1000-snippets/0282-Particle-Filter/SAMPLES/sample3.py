# sample3.py
# Particle filter for 2D position estimation with noisy distance measurements.

import numpy as np


def initialize_particles(N=1000, bounds=(-10, 10)):
    xs = np.random.uniform(bounds[0], bounds[1], size=N)
    ys = np.random.uniform(bounds[0], bounds[1], size=N)
    return np.vstack([xs, ys]).T


def weight_particles(particles, measurement, meas_std=1.0, beacon=(0, 0)):
    # measurement is the distance to a known beacon
    dist = np.linalg.norm(particles - beacon, axis=1)
    weights = np.exp(-0.5 * ((dist - measurement) / meas_std) ** 2)
    weights += 1e-12
    return weights / np.sum(weights)


def resample(particles, weights):
    N = len(particles)
    indices = np.random.choice(np.arange(N), size=N, replace=True, p=weights)
    return particles[indices]


if __name__ == '__main__':
    np.random.seed(2)
    true_pos = np.array([3.0, -2.0])
    beacon = np.array([0.0, 0.0])

    particles = initialize_particles(N=1000, bounds=(-10, 10))
    distances = np.linalg.norm(true_pos - beacon)

    estimates = []
    for step in range(5):
        measurement = distances + np.random.normal(scale=0.5)
        weights = weight_particles(particles, measurement, meas_std=0.5, beacon=beacon)
        particles = resample(particles, weights)
        estimate = particles.mean(axis=0)
        estimates.append(estimate)

    print("True position:", true_pos)
    print("Estimated positions:")
    for i, est in enumerate(estimates, start=1):
        print(f"  step {i}: {np.round(est, 3)}")
