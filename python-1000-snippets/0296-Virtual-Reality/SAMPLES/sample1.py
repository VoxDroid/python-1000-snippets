# sample1.py
# Render a simple 3D cube from two eye positions to simulate a stereo VR pair.

import numpy as np
from PIL import Image, ImageDraw


def project_points(points, K, R, t, img_size):
    # Points: (N, 3)
    pts_cam = (R @ points.T) + t
    pts_proj = K @ (pts_cam / pts_cam[2])
    pts_2d = pts_proj[:2].T
    # Normalize to pixel coords
    pts_pixel = pts_2d
    return pts_pixel


def draw_points(points_px, img_size, filename):
    img = Image.new('RGB', img_size, 'black')
    draw = ImageDraw.Draw(img)
    for x, y in points_px:
        draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill='white')
    img.save(filename)


if __name__ == '__main__':
    # 8 corners of a unit cube centered at origin
    cube_pts = np.array(
        [
            [-0.5, -0.5, -0.5],
            [0.5, -0.5, -0.5],
            [0.5, 0.5, -0.5],
            [-0.5, 0.5, -0.5],
            [-0.5, -0.5, 0.5],
            [0.5, -0.5, 0.5],
            [0.5, 0.5, 0.5],
            [-0.5, 0.5, 0.5],
        ]
    )

    # Camera intrinsics: focal length and principal point
    img_size = (400, 400)
    fx = fy = 400.0
    cx, cy = img_size[0] / 2, img_size[1] / 2
    K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])

    # Left and right eye positions (baseline)
    baseline = 0.1
    R = np.eye(3)
    t_left = np.array([[-baseline / 2], [0.0], [3.0]])
    t_right = np.array([[baseline / 2], [0.0], [3.0]])

    left_px = project_points(cube_pts, K, R, t_left, img_size)
    right_px = project_points(cube_pts, K, R, t_right, img_size)

    draw_points(left_px, img_size, '/tmp/vr_left.png')
    draw_points(right_px, img_size, '/tmp/vr_right.png')

    print('Saved stereo pair to /tmp/vr_left.png and /tmp/vr_right.png')
