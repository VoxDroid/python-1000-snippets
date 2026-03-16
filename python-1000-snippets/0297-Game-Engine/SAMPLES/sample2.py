# sample2.py
# Basic entity-component update system with simple physics and collision.

import random


class Entity:
    def __init__(self, name, position, velocity):
        self.name = name
        self.position = position
        self.velocity = velocity

    def update(self, dt):
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def step(self, dt):
        for e in self.entities:
            e.update(dt)
            # Simple boundary collision reflection
            if e.position[0] < 0 or e.position[0] > self.width:
                e.velocity[0] *= -1
            if e.position[1] < 0 or e.position[1] > self.height:
                e.velocity[1] *= -1

    def log_state(self):
        for e in self.entities:
            print(f"{e.name}: pos=({e.position[0]:.2f}, {e.position[1]:.2f}) vel=({e.velocity[0]:.2f}, {e.velocity[1]:.2f})")


if __name__ == '__main__':
    world = World(10, 10)
    for i in range(3):
        pos = [random.uniform(2, 8), random.uniform(2, 8)]
        vel = [random.uniform(-1, 1), random.uniform(-1, 1)]
        world.add_entity(Entity(f"Entity{i+1}", pos, vel))

    for step in range(5):
        print(f"\nStep {step + 1}")
        world.step(1.0)
        world.log_state()
