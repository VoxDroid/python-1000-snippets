# sample1.py
# Basic 1D particle filter estimating a constant value from noisy measurements.

import numpy as np


def resample(particles, weights):
    N = len(particles)
    indices = np.random.choice(N, size=N, replace=True, p=weights)
    return particles[indices]


def particle_filter(measurements, N=500, process_std=0.1, meas_std=0.5):
    particles = np.random.normal(0.0, 1.0, size=N)
    weights = np.ones(N) / N

    estimates = []
    for z in measurements:
        # Predict
        particles += np.random.normal(0, process_std, size=N)

        # Update weights based on measurement likelihood
        weights *= np.exp(-0.5 * ((particles - z) / meas_std) ** 2)
        weights += 1e-12  # avoid zeros
        weights /= np.sum(weights)

        # Estimate state
        estimates.append(np.sum(particles * weights))

        # Resample
        particles = resample(particles, weights)
        weights.fill(1.0 / N)

    return np.array(estimates)


if __name__ == '__main__':
    true_value = 3.0
    rng = np.random.default_rng(0)
    measurements = true_value + rng.normal(scale=0.5, size=30)

    estimates = particle_filter(measurements)

    print("First 5 measurements:", np.round(measurements[:5], 3))
    print("First 5 estimates:", np.round(estimates[:5], 3))
    print("Final estimate:", np.round(estimates[-1], 3))
