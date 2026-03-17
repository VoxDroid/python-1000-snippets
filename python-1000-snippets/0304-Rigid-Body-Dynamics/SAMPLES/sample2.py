#!/usr/bin/env python3
"""Rigid body rotation under applied torque."""


class RigidBody2D:
    def __init__(self, mass=1.0, inertia=1.0, angle=0.0):
        self.mass = float(mass)
        self.inertia = float(inertia)
        self.angle = float(angle)
        self.angular_velocity = 0.0

    def apply_torque(self, torque, dt):
        # torque = I * angular_acceleration
        angular_acc = torque / self.inertia
        self.angular_velocity += angular_acc * dt

    def step(self, dt):
        self.angle += self.angular_velocity * dt


def main():
    body = RigidBody2D(mass=1.0, inertia=2.0, angle=0.0)
    torque = 1.2  # constant torque
    dt = 0.01

    for _ in range(300):
        body.apply_torque(torque, dt)
        body.step(dt)

    print(f"Final angular velocity: {body.angular_velocity:.2f} rad/s")
    print(f"Final angle: {body.angle:.2f} rad")


if __name__ == '__main__':
    main()
