# sample3.py
# Particle system with boundary collisions (bounce) and simple damping.

import numpy as np


class BouncingParticles:
    def __init__(self, count=50, bounds=(10.0, 10.0)):
        self.count = count
        self.bounds = np.array(bounds)
        self.reset()

    def reset(self):
        self.pos = np.random.rand(self.count, 2) * self.bounds
        self.vel = (np.random.rand(self.count, 2) - 0.5) * 4.0

    def update(self, dt=0.1, damping=0.99):
        self.pos += self.vel * dt
        # Bounce on boundaries
        for i in range(self.count):
            for d in range(2):
                if self.pos[i, d] < 0:
                    self.pos[i, d] = 0
                    self.vel[i, d] *= -1
                elif self.pos[i, d] > self.bounds[d]:
                    self.pos[i, d] = self.bounds[d]
                    self.vel[i, d] *= -1
        self.vel *= damping

    def summary(self):
        return {
            "avg_pos": self.pos.mean(axis=0).tolist(),
            "avg_speed": float(np.mean(np.linalg.norm(self.vel, axis=1))),
        }


if __name__ == '__main__':
    ps = BouncingParticles(count=80, bounds=(10.0, 8.0))
    for step in range(1, 11):
        ps.update(dt=0.1)
        s = ps.summary()
        print(
            f"Step {step}: avg_pos={s['avg_pos'][0]:.2f},{s['avg_pos'][1]:.2f} "
            f"avg_speed={s['avg_speed']:.2f}"
        )
