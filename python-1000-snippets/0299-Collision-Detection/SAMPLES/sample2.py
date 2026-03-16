# sample2.py
# Circle-circle collision detection and simple response (elastic bounce) in 2D.

import numpy as np


def circle_collision(c1, r1, c2, r2):
    return np.linalg.norm(np.array(c1) - np.array(c2)) < (r1 + r2)


def resolve_collision(c1, v1, r1, c2, v2, r2):
    # Swap velocities for an elastic approximation
    return v2, v1


if __name__ == '__main__':
    c1, r1, v1 = np.array([0.0, 0.0]), 1.0, np.array([1.0, 0.0])
    c2, r2, v2 = np.array([2.0, 0.0]), 1.0, np.array([-1.0, 0.0])

    print('Before:', c1, v1, c2, v2)
    if circle_collision(c1, r1, c2, r2):
        v1, v2 = resolve_collision(c1, v1, r1, c2, v2, r2)
    print('After:', c1, v1, c2, v2)

    # Move them slightly and test again
    c1 += v1 * 0.5
    c2 += v2 * 0.5
    print('Moved:', c1, c2)
    print('Collision now:', circle_collision(c1, r1, c2, r2))
