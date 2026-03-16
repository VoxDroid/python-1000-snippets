# sample3.py
# Ray-sphere intersection in 3D.

import numpy as np


def ray_sphere_intersect(origin, direction, center, radius):
    # Solve quadratic equation for intersection
    # (o + t*d - c)^2 = r^2
    oc = origin - center
    a = np.dot(direction, direction)
    b = 2.0 * np.dot(oc, direction)
    c = np.dot(oc, oc) - radius * radius
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return False, None
    t0 = (-b - np.sqrt(discriminant)) / (2 * a)
    t1 = (-b + np.sqrt(discriminant)) / (2 * a)
    t = min(t0, t1)
    if t < 0:
        t = max(t0, t1)
    if t < 0:
        return False, None
    return True, t


if __name__ == '__main__':
    origin = np.array([0.0, 0.0, 0.0])
    direction = np.array([1.0, 0.5, 0.2])
    direction = direction / np.linalg.norm(direction)

    center = np.array([5.0, 2.0, 1.0])
    radius = 1.5

    hit, t = ray_sphere_intersect(origin, direction, center, radius)
    print('Hit:', hit)
    if hit:
        point = origin + direction * t
        print('Hit distance t:', t)
        print('Hit point:', point)
