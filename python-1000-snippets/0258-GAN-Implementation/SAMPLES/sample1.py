# sample1.py
# Simple GAN components: generator + discriminator forward passes.

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def generator(z, Wg, bg):
    # Simple linear generator: z (batch, 2) -> output (batch, 1)
    return z @ Wg + bg


def discriminator(x, Wd, bd):
    # Simple linear discriminator: x (batch, 1) -> probability (batch, 1)
    logits = x @ Wd + bd
    return sigmoid(logits)


if __name__ == '__main__':
    np.random.seed(0)

    # Random weights for generator and discriminator
    Wg = np.random.randn(2, 1) * 0.5
    bg = np.zeros(1)
    Wd = np.random.randn(1, 1) * 0.5
    bd = np.zeros(1)

    # Sample random noise
    z = np.random.randn(5, 2)
    fake = generator(z, Wg, bg)

    # Discriminator scores
    d_fake = discriminator(fake, Wd, bd)

    print("Noise (first 3):")
    print(z[:3])
    print("Generated samples (first 3):")
    print(fake[:3])
    print("Discriminator probabilities (first 3):")
    print(d_fake[:3])
