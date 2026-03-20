# sample3.py
# Perform point-in-bounding-box checks on geospatial coordinates.

from __future__ import annotations


def point_in_bbox(point, bbox):
    lat, lon = point
    min_lat, min_lon, max_lat, max_lon = bbox
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


def main() -> None:
    bbox = (25.0, -130.0, 50.0, -60.0)  # approximate continental US
    points = [
        (37.7749, -122.4194),  # San Francisco
        (47.6062, -122.3321),  # Seattle
        (19.4326, -99.1332),   # Mexico City
    ]
    for p in points:
        status = "inside" if point_in_bbox(p, bbox) else "outside"
        print(f"Point {p} is {status} the bbox")


if __name__ == '__main__':
    main()
