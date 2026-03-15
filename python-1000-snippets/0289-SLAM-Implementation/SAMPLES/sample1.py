# sample1.py
# Simple 2D EKF-SLAM example with two static landmarks.

import numpy as np


def normalize_angle(angle):
    """Normalize angle to [-pi, pi]."""
    return (angle + np.pi) % (2 * np.pi) - np.pi


def motion_model(x, u, dt=1.0):
    """Compute new pose given control u = [v, omega]."""
    x_r, y_r, theta = x
    v, omega = u
    if abs(omega) < 1e-9:
        x_r += v * dt * np.cos(theta)
        y_r += v * dt * np.sin(theta)
    else:
        x_r += (v / omega) * (np.sin(theta + omega * dt) - np.sin(theta))
        y_r += (v / omega) * (-np.cos(theta + omega * dt) + np.cos(theta))
        theta += omega * dt
    return np.array([x_r, y_r, normalize_angle(theta)])


def observation_model(x, landmark_pos):
    """Return range and bearing to a landmark from robot pose."""
    dx = landmark_pos[0] - x[0]
    dy = landmark_pos[1] - x[1]
    r = np.hypot(dx, dy)
    bearing = normalize_angle(np.arctan2(dy, dx) - x[2])
    return np.array([r, bearing])


def ekf_predict(mu, sigma, u, motion_noise):
    """EKF predict step for robot pose only (landmarks remain fixed)."""
    x_r, y_r, theta = mu[:3]
    v, omega = u

    # Motion jacobian (robot pose block)
    G = np.eye(len(mu))
    if abs(omega) < 1e-9:
        G[0, 2] = -v * np.sin(theta)
        G[1, 2] = v * np.cos(theta)
    else:
        G[0, 2] = (v / omega) * (np.cos(theta + omega) - np.cos(theta))
        G[1, 2] = (v / omega) * (np.sin(theta + omega) - np.sin(theta))

    # Noise in control (robot pose block only)
    R = np.zeros_like(sigma)
    R[:3, :3] = motion_noise

    mu[:3] = motion_model(mu[:3], u)
    sigma = G @ sigma @ G.T + R
    return mu, sigma


def ekf_update(mu, sigma, z, landmark_idx, measure_noise):
    """EKF update step for a single landmark measurement."""
    # landmark state start index
    lm_idx = 3 + 2 * landmark_idx
    lm_pos = mu[lm_idx:lm_idx + 2]

    # Expected measurement
    z_hat = observation_model(mu[:3], lm_pos)

    # Measurement Jacobian
    dx = lm_pos[0] - mu[0]
    dy = lm_pos[1] - mu[1]
    q = dx * dx + dy * dy
    sqrt_q = np.sqrt(q)

    H = np.zeros((2, len(mu)))
    H[0, 0] = -dx / sqrt_q
    H[0, 1] = -dy / sqrt_q
    H[0, lm_idx + 0] = dx / sqrt_q
    H[0, lm_idx + 1] = dy / sqrt_q

    H[1, 0] = dy / q
    H[1, 1] = -dx / q
    H[1, 2] = -1
    H[1, lm_idx + 0] = -dy / q
    H[1, lm_idx + 1] = dx / q

    S = H @ sigma @ H.T + measure_noise
    K = sigma @ H.T @ np.linalg.inv(S)

    dz = z - z_hat
    dz[1] = normalize_angle(dz[1])

    mu = mu + K @ dz
    mu[2] = normalize_angle(mu[2])
    sigma = (np.eye(len(mu)) - K @ H) @ sigma
    return mu, sigma


if __name__ == '__main__':
    np.random.seed(0)

    # Ground truth landmarks (unknown to the robot)
    landmarks = np.array([[2.0, 1.0], [4.0, 3.5]])

    # EKF-SLAM state: [x, y, theta, lm1_x, lm1_y, lm2_x, lm2_y]
    mu = np.array([0.0, 0.0, 0.0, 1.0, 1.0, 3.0, 3.0])
    sigma = np.eye(len(mu)) * 1e-3
    sigma[3:, 3:] *= 100.0  # large uncertainty for landmarks

    motion_noise = np.diag([0.05, 0.05, np.deg2rad(1.0)]) ** 2
    measure_noise = np.diag([0.1, np.deg2rad(3.0)]) ** 2

    controls = [
        (0.8, np.deg2rad(10.0)),
        (0.8, np.deg2rad(5.0)),
        (0.8, np.deg2rad(-8.0)),
        (0.7, np.deg2rad(0.0)),
    ]

    for step, u in enumerate(controls, start=1):
        # Predict
        mu, sigma = ekf_predict(mu, sigma, u, motion_noise)

        # Simulate noisy observations to each landmark
        for i, lm in enumerate(landmarks):
            z_true = observation_model(mu[:3], lm)
            z = z_true + np.array([np.random.normal(scale=0.1), np.random.normal(scale=np.deg2rad(3.0))])
            mu, sigma = ekf_update(mu, sigma, z, i, measure_noise)

        print(f"Step {step}: pose = [{mu[0]:.2f}, {mu[1]:.2f}, {np.rad2deg(mu[2]):.1f} deg]")

    print("\nFinal estimated landmarks:")
    for i in range(len(landmarks)):
        idx = 3 + 2 * i
        print(f"  Landmark {i+1}: ({mu[idx]:.2f}, {mu[idx+1]:.2f})")

    print("\nGround truth landmarks:")
    for i, lm in enumerate(landmarks, start=1):
        print(f"  Landmark {i}: ({lm[0]:.2f}, {lm[1]:.2f})")
