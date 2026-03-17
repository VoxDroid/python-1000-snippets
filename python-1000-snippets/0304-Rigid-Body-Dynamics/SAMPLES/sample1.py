#!/usr/bin/env python3
"""Simple rigid body drop under gravity."""

import math


class RigidBody2D:
    def __init__(self, mass=1.0, inertia=1.0, position=(0.0, 0.0), angle=0.0):
        self.mass = float(mass)
        self.inv_mass = 1.0 / self.mass
        self.inertia = float(inertia)
        self.inv_inertia = 1.0 / self.inertia
        self.position = list(position)
        self.angle = float(angle)
        self.velocity = [0.0, 0.0]
        self.angular_velocity = 0.0

    def apply_force(self, force, dt):
        # force is (fx, fy)
        self.velocity[0] += (force[0] * self.inv_mass) * dt
        self.velocity[1] += (force[1] * self.inv_mass) * dt

    def apply_torque(self, torque, dt):
        self.angular_velocity += torque * self.inv_inertia * dt

    def step(self, dt):
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt
        self.angle += self.angular_velocity * dt


def run_drop_simulation():
    body = RigidBody2D(mass=1.0, inertia=1.0, position=(0.0, 2.0), angle=0.0)
    gravity = (0.0, -9.8)
    dt = 0.01

    for _ in range(300):
        body.apply_force(gravity, dt)
        body.step(dt)
        # simple ground collision
        if body.position[1] < 0.0:
            body.position[1] = 0.0
            if body.velocity[1] < 0.0:
                body.velocity[1] *= -0.6

    return body


def main():
    body = run_drop_simulation()
    print(f"Final pos: ({body.position[0]:.2f}, {body.position[1]:.2f}), angle: {body.angle:.2f} rad")


if __name__ == '__main__':
    main()
