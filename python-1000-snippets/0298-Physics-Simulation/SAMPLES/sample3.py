# sample3.py
# Particle collision simulation with simple elastic collisions in 2D.

import numpy as np


def simulate(num_particles=5, steps=10, dt=0.1, bounds=(10, 10)):
    np.random.seed(0)
    pos = np.random.rand(num_particles, 2) * bounds
    vel = (np.random.rand(num_particles, 2) - 0.5) * 2.0

    for step in range(steps):
        # Integrate motion
        pos += vel * dt

        # Wall collisions (elastic)
        for i in range(num_particles):
            if pos[i, 0] < 0 or pos[i, 0] > bounds[0]:
                vel[i, 0] *= -1
            if pos[i, 1] < 0 or pos[i, 1] > bounds[1]:
                vel[i, 1] *= -1

        # Simple pairwise collision (swap velocities)
        for i in range(num_particles):
            for j in range(i + 1, num_particles):
                if np.linalg.norm(pos[i] - pos[j]) < 0.5:
                    vel[i], vel[j] = vel[j].copy(), vel[i].copy()

        print(f"Step {step + 1}")
        for i in range(num_particles):
            print(f"  P{i}: pos=({pos[i,0]:.2f},{pos[i,1]:.2f}) vel=({vel[i,0]:.2f},{vel[i,1]:.2f})")


if __name__ == '__main__':
    simulate()
