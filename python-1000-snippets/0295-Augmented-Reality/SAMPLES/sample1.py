# sample1.py
# Simple augmented reality overlay: detect a square marker and draw a virtual cube overlay.

import cv2
import numpy as np


def create_marker_image():
    img = np.zeros((300, 400, 3), dtype=np.uint8)
    # Draw a white square marker
    cv2.rectangle(img, (120, 80), (280, 240), (255, 255, 255), -1)
    return img


def find_square_contour(img_gray):
    thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        if len(approx) == 4 and cv2.contourArea(approx) > 1000:
            return approx.reshape((4, 2))
    return None


def draw_cube(img, pts):
    # Draw a simple 3D cube using the marker corners as the base
    # Assume pts are in order (tl, tr, br, bl)
    tl, tr, br, bl = pts
    offset = np.array([0, -50])
    # top of cube
    t_tl = tl + offset
    t_tr = tr + offset
    t_br = br + offset
    t_bl = bl + offset
    # Draw base square
    cv2.polylines(img, [pts.astype(int)], True, (0, 255, 0), 2)
    # Draw top square
    cv2.polylines(img, [np.array([t_tl, t_tr, t_br, t_bl], dtype=int)], True, (0, 255, 0), 2)
    # Connect edges
    for a, b in zip([tl, tr, br, bl], [t_tl, t_tr, t_br, t_bl]):
        cv2.line(img, tuple(a.astype(int)), tuple(b.astype(int)), (0, 255, 0), 2)


if __name__ == '__main__':
    img = create_marker_image()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = find_square_contour(gray)
    if corners is not None:
        draw_cube(img, corners)
        print('Marker found and overlay drawn.')
    else:
        print('Marker not detected.')

    # Uncomment to display the result if GUI is available
    # cv2.imshow('AR Overlay', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
