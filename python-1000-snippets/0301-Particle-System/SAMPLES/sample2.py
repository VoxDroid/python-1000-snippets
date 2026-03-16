# sample2.py
# Particle fountain: particles are emitted upward and affected by gravity.

import numpy as np


class Fountain:
    def __init__(self, count=200, spread=1.0):
        self.count = count
        self.spread = spread
        self.reset()

    def reset(self):
        self.pos = np.zeros((self.count, 2))
        angles = np.random.uniform(-0.3, 0.3, size=self.count)
        speeds = np.random.uniform(2.0, 5.0, size=self.count)
        self.vel = np.stack([speeds * np.sin(angles), speeds * np.cos(angles)], axis=1)
        self.age = np.zeros(self.count)
        self.life = np.random.uniform(1.0, 2.5, size=self.count)

    def update(self, dt=0.02):
        # Gravity pulls downward in y
        g = np.array([0.0, -9.81])
        self.vel += g * dt
        self.pos += self.vel * dt
        self.age += dt

        dead = self.age >= self.life
        if np.any(dead):
            self.pos[dead] = 0.0
            angles = np.random.uniform(-0.3, 0.3, size=np.sum(dead))
            speeds = np.random.uniform(2.0, 5.0, size=np.sum(dead))
            self.vel[dead] = np.stack([speeds * np.sin(angles), speeds * np.cos(angles)], axis=1)
            self.age[dead] = 0.0
            self.life[dead] = np.random.uniform(1.0, 2.5, size=np.sum(dead))

    def summary(self):
        return {
            "avg_pos": self.pos.mean(axis=0).tolist(),
            "avg_vel": self.vel.mean(axis=0).tolist(),
            "alive": float(np.mean(self.age < self.life)),
        }


if __name__ == '__main__':
    fountain = Fountain(count=300)
    for step in range(1, 11):
        fountain.update(dt=0.05)
        s = fountain.summary()
        print(
            f"Step {step}: avg_pos={s['avg_pos'][0]:.2f},{s['avg_pos'][1]:.2f} "
            f"avg_vel={s['avg_vel'][0]:.2f},{s['avg_vel'][1]:.2f} "
            f"alive={s['alive']:.2f}"
        )
