# sample3.py
# Demonstrate fusing two independent sensor estimates using covariance-weighted fusion.

import numpy as np


def fuse_two_estimates(x1, P1, x2, P2):
    """Fuse two Gaussian estimates (scalar) using covariance weighting."""
    P1_inv = 1.0 / P1
    P2_inv = 1.0 / P2
    x = (x1 * P1_inv + x2 * P2_inv) / (P1_inv + P2_inv)
    P = 1.0 / (P1_inv + P2_inv)
    return x, P


if __name__ == '__main__':
    np.random.seed(0)

    true_value = 10.0
    sensor1_var = 0.5 ** 2  # higher noise
    sensor2_var = 0.2 ** 2  # lower noise

    x1 = 0.0
    x2 = 0.0
    P1 = sensor1_var
    P2 = sensor2_var

    print('Step  Sensor1  Sensor2  Fused  True')
    for step in range(1, 11):
        z1 = true_value + np.random.normal(scale=np.sqrt(sensor1_var))
        z2 = true_value + np.random.normal(scale=np.sqrt(sensor2_var))

        x1, P1 = fuse_two_estimates(x1, P1, z1, sensor1_var)
        x2, P2 = fuse_two_estimates(x2, P2, z2, sensor2_var)

        fused, fused_var = fuse_two_estimates(x1, P1, x2, P2)
        print(f"{step:2d}  {z1:.2f}    {z2:.2f}    {fused:.2f}  {true_value:.2f}")
