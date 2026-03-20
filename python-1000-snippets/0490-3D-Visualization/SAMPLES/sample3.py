# sample3.py
# Compute simple properties of a 3D mesh and print summary statistics.

from __future__ import annotations


def compute_centroid(vertices: list[tuple[float, float, float]]) -> tuple[float, float, float]:
    n = len(vertices)
    sx = sum(v[0] for v in vertices)
    sy = sum(v[1] for v in vertices)
    sz = sum(v[2] for v in vertices)
    return (sx / n, sy / n, sz / n)


def compute_bounds(vertices: list[tuple[float, float, float]]):
    xs = [v[0] for v in vertices]
    ys = [v[1] for v in vertices]
    zs = [v[2] for v in vertices]
    return (min(xs), max(xs)), (min(ys), max(ys)), (min(zs), max(zs))


def main() -> None:
    # Example: a simple cube mesh.
    vertices = [
        (-1, -1, -1),
        (-1, -1, 1),
        (-1, 1, -1),
        (-1, 1, 1),
        (1, -1, -1),
        (1, -1, 1),
        (1, 1, -1),
        (1, 1, 1),
    ]
    centroid = compute_centroid(vertices)
    bounds = compute_bounds(vertices)
    print("Mesh vertices:", len(vertices))
    print("Centroid:", centroid)
    print("Bounds:")
    print("  x:", bounds[0])
    print("  y:", bounds[1])
    print("  z:", bounds[2])


if __name__ == "__main__":
    main()
