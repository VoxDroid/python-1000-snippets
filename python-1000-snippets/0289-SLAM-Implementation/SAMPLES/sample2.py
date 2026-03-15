# sample2.py
# Simple Particle Filter SLAM for 2D robot with two landmarks.

import numpy as np


def normalize_angle(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def motion_update(pose, u, dt=1.0):
    x, y, theta = pose
    v, omega = u
    if abs(omega) < 1e-9:
        x += v * dt * np.cos(theta)
        y += v * dt * np.sin(theta)
    else:
        x += (v / omega) * (np.sin(theta + omega * dt) - np.sin(theta))
        y += (v / omega) * (-np.cos(theta + omega * dt) + np.cos(theta))
        theta += omega * dt
    return np.array([x, y, normalize_angle(theta)])


def measurement_model(pose, landmark):
    dx = landmark[0] - pose[0]
    dy = landmark[1] - pose[1]
    r = np.hypot(dx, dy)
    bearing = normalize_angle(np.arctan2(dy, dx) - pose[2])
    return np.array([r, bearing])


def weight_measurement(pose, landmark, z, noise_cov):
    z_hat = measurement_model(pose, landmark)
    dz = z - z_hat
    dz[1] = normalize_angle(dz[1])
    cov_inv = np.linalg.inv(noise_cov)
    return np.exp(-0.5 * dz.T @ cov_inv @ dz)


if __name__ == '__main__':
    np.random.seed(0)
    true_landmarks = np.array([[2.0, 1.0], [4.0, 3.5]])

    num_particles = 200
    particles = np.zeros((num_particles, 3 + 2 * len(true_landmarks)))
    # Initialize robot pose around origin and landmarks randomly
    particles[:, 0:3] = np.random.normal([0.0, 0.0, 0.0], [0.1, 0.1, np.deg2rad(5.0)], size=(num_particles, 3))
    particles[:, 3:] = np.array([1.0, 1.0, 3.0, 3.0]) + np.random.normal(0, 0.5, size=(num_particles, 4))

    motion_noise = np.diag([0.05, 0.05, np.deg2rad(2.0)]) ** 2
    measure_noise = np.diag([0.1, np.deg2rad(5.0)]) ** 2

    controls = [(0.8, np.deg2rad(10.0)), (0.8, np.deg2rad(5.0)), (0.8, np.deg2rad(-8.0)), (0.7, 0.0)]

    for step, u in enumerate(controls, start=1):
        # Predict
        for i in range(num_particles):
            noisy_u = u + np.random.multivariate_normal(np.zeros(3), motion_noise)[:2]
            particles[i, 0:3] = motion_update(particles[i, 0:3], noisy_u)

        # Generate observations from true pose
        # (simulate as if we had perfect odometry and noisy landmarks)
        # In a real system, these would come from sensors.
        # We assume the robot's true pose is the mean of the particles.
        true_pose = particles[:, 0:3].mean(axis=0)
        observations = []
        for lm in true_landmarks:
            z = measurement_model(true_pose, lm)
            z += np.array([np.random.normal(scale=0.1), np.random.normal(scale=np.deg2rad(5.0))])
            observations.append(z)

        # Update weights based on measurement likelihood
        weights = np.ones(num_particles)
        for z, lm_idx in zip(observations, range(len(true_landmarks))):
            lm_pos = particles[:, 3 + 2 * lm_idx: 3 + 2 * lm_idx + 2]
            for i in range(num_particles):
                weights[i] *= weight_measurement(particles[i, 0:3], lm_pos[i], z, measure_noise)

        weights += 1e-300
        weights /= weights.sum()

        # Resample
        indices = np.random.choice(num_particles, size=num_particles, p=weights)
        particles = particles[indices]

        mean_pose = particles[:, 0:3].mean(axis=0)
        print(f"Step {step}: pose ~ [{mean_pose[0]:.2f}, {mean_pose[1]:.2f}, {np.rad2deg(mean_pose[2]):.1f} deg]")

    print("\nEstimated landmarks (particle mean):")
    mean_landmarks = particles[:, 3:].mean(axis=0)
    for i in range(len(true_landmarks)):
        print(f"  Landmark {i+1}: ({mean_landmarks[2*i]:.2f}, {mean_landmarks[2*i+1]:.2f})")

    print("\nGround truth landmarks:")
    for i, lm in enumerate(true_landmarks, 1):
        print(f"  Landmark {i}: ({lm[0]:.2f}, {lm[1]:.2f})")
