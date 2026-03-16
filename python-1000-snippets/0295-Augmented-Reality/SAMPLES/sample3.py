# sample3.py
# Project a texture onto a planar surface (homography warping) to simulate AR overlay.

import cv2
import numpy as np


def create_scene():
    # Create a scene with a planar rectangle (target surface)
    img = np.zeros((400, 600, 3), dtype=np.uint8)
    # Draw the target plane rectangle
    cv2.rectangle(img, (150, 100), (450, 300), (50, 50, 50), -1)
    return img


def create_texture():
    # Create a simple texture to overlay
    tex = np.zeros((200, 300, 3), dtype=np.uint8)
    for i in range(0, 300, 30):
        color = (0, 255, 255) if (i // 30) % 2 == 0 else (255, 0, 255)
        cv2.line(tex, (i, 0), (i, 200), color, 2)
    return tex


if __name__ == '__main__':
    scene = create_scene()
    tex = create_texture()

    # Define correspondences (corners of the rectangle in the scene)
    src = np.array([[0, 0], [tex.shape[1], 0], [tex.shape[1], tex.shape[0]], [0, tex.shape[0]]], dtype=np.float32)
    dst = np.array([[150, 100], [450, 100], [450, 300], [150, 300]], dtype=np.float32)

    H, _ = cv2.findHomography(src, dst)
    warped = cv2.warpPerspective(tex, H, (scene.shape[1], scene.shape[0]))

    # Overlay the warped texture onto the scene
    mask = (warped.sum(axis=2) > 0).astype(np.uint8)
    scene[mask == 1] = warped[mask == 1]

    print('Homography matrix:')
    print(H)
    # Uncomment to visualize
    # cv2.imshow('AR Projection', scene)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
