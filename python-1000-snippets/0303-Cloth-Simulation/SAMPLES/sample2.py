#!/usr/bin/env python3
"""Cloth simulation sample that exports an image of the cloth state."""

import numpy as np
from PIL import Image, ImageDraw


class Cloth:
    def __init__(self, width, height, spacing=1.0, fixed_indices=None):
        self.w = width
        self.h = height
        self.spacing = float(spacing)
        self.positions = np.zeros((height, width, 2), dtype=float)
        self.prev_positions = np.zeros_like(self.positions)

        for y in range(height):
            for x in range(width):
                self.positions[y, x] = np.array([x * self.spacing, y * self.spacing])
        self.prev_positions[:] = self.positions

        self.fixed = np.zeros((height, width), dtype=bool)
        if fixed_indices is None:
            self.fixed[0, :] = True
        else:
            for (y, x) in fixed_indices:
                self.fixed[y, x] = True

        self.rest_length = self.spacing

    def step(self, dt=0.02, gravity=(0.0, 9.8), damping=0.99, constraint_iters=5):
        current = self.positions
        previous = self.prev_positions
        velocity = (current - previous) * damping
        acceleration = np.array(gravity, dtype=float)

        next_pos = current + velocity + acceleration * (dt * dt)
        self.prev_positions = current.copy()
        self.positions = next_pos

        for _ in range(constraint_iters):
            self._satisfy_constraints()
            self.positions[self.fixed] = self.prev_positions[self.fixed]

    def _satisfy_constraints(self):
        for y in range(self.h):
            for x in range(self.w):
                if x + 1 < self.w:
                    self._satisfy_spring(y, x, y, x + 1)
                if y + 1 < self.h:
                    self._satisfy_spring(y, x, y + 1, x)
                if x + 1 < self.w and y + 1 < self.h:
                    self._satisfy_spring(y, x, y + 1, x + 1)
                if x > 0 and y + 1 < self.h:
                    self._satisfy_spring(y, x, y + 1, x - 1)

    def _satisfy_spring(self, y1, x1, y2, x2):
        p1 = self.positions[y1, x1]
        p2 = self.positions[y2, x2]
        delta = p2 - p1
        dist = np.linalg.norm(delta)
        if dist == 0:
            return
        diff = (dist - self.rest_length) / dist
        correction = delta * 0.5 * diff

        if not self.fixed[y1, x1]:
            self.positions[y1, x1] += correction
        if not self.fixed[y2, x2]:
            self.positions[y2, x2] -= correction


def draw_cloth(cloth, output_path='/tmp/cloth.png', img_size=(400, 400)):
    scale = min(img_size[0] / (cloth.w - 1), img_size[1] / (cloth.h - 1)) * 0.9
    offset = np.array([20.0, 20.0])

    img = Image.new('RGB', img_size, (255, 255, 255))
    draw = ImageDraw.Draw(img)

    def to_image(p):
        return tuple((p * scale + offset).astype(int))

    for y in range(cloth.h):
        for x in range(cloth.w):
            if x + 1 < cloth.w:
                draw.line([to_image(cloth.positions[y, x]), to_image(cloth.positions[y, x + 1])], fill='black')
            if y + 1 < cloth.h:
                draw.line([to_image(cloth.positions[y, x]), to_image(cloth.positions[y + 1, x])], fill='black')

    img.save(output_path)
    return output_path


def main():
    cloth = Cloth(width=8, height=8, spacing=1.0)

    for _ in range(150):
        cloth.step(dt=0.02)

    out_path = draw_cloth(cloth)
    print(f"Saved {out_path}")


if __name__ == '__main__':
    main()
