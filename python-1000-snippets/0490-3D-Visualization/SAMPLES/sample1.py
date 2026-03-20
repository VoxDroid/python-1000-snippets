# sample1.py
# Generate a simple 3D point cloud (cube vertices) and save it as a PLY file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../../temp/cube.ply")


def generate_cube_vertices(size: float = 1.0):
    # Cube centered at origin with side length `size`.
    hs = size / 2.0
    return [
        (-hs, -hs, -hs),
        (-hs, -hs, hs),
        (-hs, hs, -hs),
        (-hs, hs, hs),
        (hs, -hs, -hs),
        (hs, -hs, hs),
        (hs, hs, -hs),
        (hs, hs, hs),
    ]


def write_ply(path: str, vertices: list[tuple[float, float, float]]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write("ply\nformat ascii 1.0\n")
        f.write(f"element vertex {len(vertices)}\n")
        f.write("property float x\nproperty float y\nproperty float z\n")
        f.write("end_header\n")
        for x, y, z in vertices:
            f.write(f"{x} {y} {z}\n")


def main() -> None:
    vertices = generate_cube_vertices(2.0)
    write_ply(OUTPUT_PATH, vertices)
    print("Saved cube point cloud to", OUTPUT_PATH)


if __name__ == "__main__":
    main()
