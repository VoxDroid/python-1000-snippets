# sample2.py
# Compute great-circle distance between two points using the haversine formula.

from __future__ import annotations
import math


def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2) ** 2 + math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) * math.sin(dlon/2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def main() -> None:
    ny = (40.7128, -74.0060)
    la = (34.0522, -118.2437)
    dist = haversine(ny[0], ny[1], la[0], la[1])
    print(f"Distance New York -> Los Angeles: {dist:.1f} km")


if __name__ == '__main__':
    main()
