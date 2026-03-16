# sample1.py
# Basic particle system: update positions with velocity and lifespan.

import numpy as np


class ParticleSystem:
    def __init__(self, count=100):
        # Structured array: position (x,y), velocity (vx,vy), age, lifetime
        self.particles = np.zeros(count, dtype=[
            ("pos", float, 2),
            ("vel", float, 2),
            ("age", float),
            ("life", float),
        ])
        self.reset()

    def reset(self):
        self.particles["pos"] = np.random.rand(len(self.particles), 2) * 10.0
        self.particles["vel"] = (np.random.rand(len(self.particles), 2) - 0.5) * 2.0
        self.particles["age"] = 0.0
        self.particles["life"] = np.random.uniform(2.0, 5.0, size=len(self.particles))

    def update(self, dt=0.1):
        self.particles["pos"] += self.particles["vel"] * dt
        self.particles["age"] += dt
        # Reset dead particles
        dead = self.particles["age"] >= self.particles["life"]
        if np.any(dead):
            self.particles[dead]["pos"] = np.random.rand(np.sum(dead), 2) * 10.0
            self.particles[dead]["vel"] = (np.random.rand(np.sum(dead), 2) - 0.5) * 2.0
            self.particles[dead]["age"] = 0.0
            self.particles[dead]["life"] = np.random.uniform(2.0, 5.0, size=np.sum(dead))

    def summary(self):
        pos = self.particles["pos"]
        vel = self.particles["vel"]
        return {
            "count": len(self.particles),
            "avg_pos": np.mean(pos, axis=0).tolist(),
            "avg_vel": np.mean(vel, axis=0).tolist(),
            "alive_ratio": float(np.mean(self.particles["age"] < self.particles["life"])),
        }


if __name__ == '__main__':
    ps = ParticleSystem(count=200)
    for frame in range(1, 11):
        ps.update(dt=0.1)
        s = ps.summary()
        print(
            f"Frame {frame}: avg_pos={s['avg_pos'][0]:.2f},{s['avg_pos'][1]:.2f} "
            f"avg_vel={s['avg_vel'][0]:.2f},{s['avg_vel'][1]:.2f} "
            f"alive={s['alive_ratio']:.2f}"
        )
