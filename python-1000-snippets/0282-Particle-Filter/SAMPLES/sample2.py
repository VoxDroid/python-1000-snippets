# sample2.py
# Demonstrate resampling degeneracy and effective sample size.

import numpy as np


def effective_sample_size(weights):
    return 1.0 / np.sum(weights ** 2)


def systematic_resample(particles, weights):
    N = len(particles)
    positions = (np.arange(N) + np.random.random()) / N
    indexes = np.zeros(N, 'i')
    cumulative_sum = np.cumsum(weights)
    i, j = 0, 0
    while i < N:
        if positions[i] < cumulative_sum[j]:
            indexes[i] = j
            i += 1
        else:
            j += 1
    return particles[indexes]


if __name__ == '__main__':
    rng = np.random.default_rng(1)
    N = 500
    particles = rng.normal(0, 1, N)
    weights = np.ones(N) / N

    # Artificially skew weights to show degeneracy
    weights *= np.exp(-0.5 * (particles - 2) ** 2 / 0.1)
    weights /= np.sum(weights)

    ess_before = effective_sample_size(weights)
    particles_resampled = systematic_resample(particles, weights)
    weights_resampled = np.ones(N) / N
    ess_after = effective_sample_size(weights_resampled)

    print(f"Effective sample size before resampling: {ess_before:.1f}")
    print(f"Effective sample size after resampling: {ess_after:.1f}")
    print(f"Mean before: {np.mean(particles):.3f}, after: {np.mean(particles_resampled):.3f}")
