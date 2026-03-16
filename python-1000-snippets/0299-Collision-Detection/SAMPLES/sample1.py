# sample1.py
# Axis-aligned bounding box (AABB) collision detection.


def aabb_intersect(a, b):
    # A and B are (x, y, w, h)
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return (ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by)


if __name__ == '__main__':
    box1 = (0, 0, 2, 2)
    box2 = (1, 1, 2, 2)
    box3 = (3, 3, 1, 1)

    print('Box1 vs Box2 intersect:', aabb_intersect(box1, box2))
    print('Box1 vs Box3 intersect:', aabb_intersect(box1, box3))
