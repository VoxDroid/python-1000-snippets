# sample1.py
# Read sample latitude/longitude points and compute centroid.

from __future__ import annotations


def sample_points():
    return [
        (40.7128, -74.0060),  # New York
        (34.0522, -118.2437), # Los Angeles
        (41.8781, -87.6298),  # Chicago
        (29.7604, -95.3698),  # Houston
    ]


def centroid(points):
    lat = sum(p[0] for p in points) / len(points)
    lng = sum(p[1] for p in points) / len(points)
    return (lat, lng)


def main() -> None:
    pts = sample_points()
    center = centroid(pts)
    print("Points:")
    for p in pts:
        print("  ", p)
    print("Centroid:", center)


if __name__ == '__main__':
    main()
