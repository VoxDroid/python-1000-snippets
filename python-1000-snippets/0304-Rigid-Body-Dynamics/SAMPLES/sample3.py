#!/usr/bin/env python3
"""Rigid body bounce simulation with restitution."""


class RigidBody2D:
    def __init__(self, mass=1.0, position=(0.0, 0.0)):
        self.mass = float(mass)
        self.position = list(position)
        self.velocity = [0.0, 0.0]

    def apply_force(self, force, dt):
        self.velocity[0] += force[0] / self.mass * dt
        self.velocity[1] += force[1] / self.mass * dt

    def step(self, dt):
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt


def main():
    body = RigidBody2D(mass=1.0, position=(0.0, 1.0))
    gravity = (0.0, -9.8)
    restitution = 0.7
    dt = 0.01

    peak = body.position[1]
    for _ in range(500):
        body.apply_force(gravity, dt)
        body.step(dt)

        if body.position[1] < 0.0:
            body.position[1] = 0.0
            if body.velocity[1] < 0.0:
                body.velocity[1] = -body.velocity[1] * restitution

        peak = max(peak, body.position[1])

    print(f"Peak bounce height: {peak:.2f}")
    print(f"Final position: ({body.position[0]:.2f}, {body.position[1]:.2f})")


if __name__ == '__main__':
    main()
