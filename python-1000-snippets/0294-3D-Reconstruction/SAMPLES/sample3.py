# sample3.py
# Fit a plane to a 3D point cloud using least-squares (SVD).

import numpy as np


def fit_plane(points):
    # Fit plane ax + by + cz + d = 0 to points
    # Solve for [a, b, c, d] using SVD on augmented matrix.
    A = np.c_[points[:, :3], np.ones(points.shape[0])]
    _, _, Vt = np.linalg.svd(A)
    plane = Vt[-1, :]
    # Normalize so that norm of (a,b,c) == 1
    norm = np.linalg.norm(plane[:3])
    return plane / (norm + 1e-12)


if __name__ == '__main__':
    np.random.seed(0)
    # Generate points around the plane z = 0.5*x + 0.2*y + 1
    xs = np.linspace(-2, 2, 10)
    ys = np.linspace(-2, 2, 10)
    points = []
    for x in xs:
        for y in ys:
            z = 0.5 * x + 0.2 * y + 1.0 + np.random.normal(scale=0.02)
            points.append([x, y, z])
    points = np.array(points)

    plane = fit_plane(points)
    print('Estimated plane coefficients (a, b, c, d):', plane)
    print('Plane equation: {:.3f}x + {:.3f}y + {:.3f}z + {:.3f} = 0'.format(*plane))
