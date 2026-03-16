# sample3.py
# Ray vs AABB intersection (2D) using parametric ray slab method.

import numpy as np


def ray_aabb_intersect(ray_origin, ray_dir, box_min, box_max):
    tmin = (box_min - ray_origin) / ray_dir
    tmax = (box_max - ray_origin) / ray_dir

    t1 = np.minimum(tmin, tmax)
    t2 = np.maximum(tmin, tmax)

    t_near = np.max(t1)
    t_far = np.min(t2)

    if t_near > t_far or t_far < 0:
        return False, None
    return True, t_near if t_near >= 0 else t_far


if __name__ == '__main__':
    origin = np.array([0.0, 0.0])
    direction = np.array([1.0, 0.5])
    direction /= np.linalg.norm(direction)

    box_min = np.array([2.0, 1.0])
    box_max = np.array([4.0, 3.0])

    hit, t = ray_aabb_intersect(origin, direction, box_min, box_max)
    print('Ray hit:', hit)
    if hit:
        hit_point = origin + direction * t
        print('Hit distance t =', t)
        print('Hit point:', hit_point)
