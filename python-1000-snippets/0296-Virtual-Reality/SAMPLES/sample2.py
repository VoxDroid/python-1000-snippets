# sample2.py
# Simulate a simple head rotation in a VR scene by rotating a basic 3D point cloud.

import numpy as np
from PIL import Image, ImageDraw


def rotate_points(points, angle_rad):
    R = np.array([
        [np.cos(angle_rad), 0, np.sin(angle_rad)],
        [0, 1, 0],
        [-np.sin(angle_rad), 0, np.cos(angle_rad)],
    ])
    return points @ R.T


def project(points, K, t):
    pts_cam = points.T + t
    pts_proj = K @ (pts_cam / pts_cam[2])
    return pts_proj[:2].T


def draw(points_px, img_size, filename):
    img = Image.new('RGB', img_size, 'black')
    draw = ImageDraw.Draw(img)
    for x, y in points_px:
        draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill='white')
    img.save(filename)


if __name__ == '__main__':
    # Generate a simple grid of 3D points
    xs = np.linspace(-0.5, 0.5, 10)
    ys = np.linspace(-0.5, 0.5, 10)
    Z = 2.0
    points = np.array([[x, y, Z] for x in xs for y in ys])

    img_size = (400, 400)
    fx = fy = 400.0
    cx, cy = img_size[0] / 2, img_size[1] / 2
    K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])

    t = np.array([[0.0], [0.0], [0.0]])

    for i, angle_deg in enumerate([0, 15, 30], start=1):
        pts_rot = rotate_points(points, np.deg2rad(angle_deg))
        pts_px = project(pts_rot, K, t)
        draw(pts_px, img_size, f'/tmp/vr_headpose_{i}.png')
        print(f'Saved head pose image {i} (angle {angle_deg} deg)')
