# sample2.py
# Create a simple heightmap surface mesh and save it as an OBJ file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../../temp/heightmap.obj")


def generate_heightmap(grid_size: int = 20, scale: float = 1.0):
    vertices = []
    faces = []
    for iy in range(grid_size):
        for ix in range(grid_size):
            x = (ix / (grid_size - 1) - 0.5) * scale
            y = (iy / (grid_size - 1) - 0.5) * scale
            z = 0.2 * ((x ** 2 + y ** 2) ** 0.5)
            vertices.append((x, y, z))
    for iy in range(grid_size - 1):
        for ix in range(grid_size - 1):
            a = iy * grid_size + ix
            b = iy * grid_size + (ix + 1)
            c = (iy + 1) * grid_size + (ix + 1)
            d = (iy + 1) * grid_size + ix
            faces.append((a, b, c))
            faces.append((a, c, d))
    return vertices, faces


def write_obj(path: str, vertices, faces):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for x, y, z in vertices:
            f.write(f"v {x} {y} {z}\n")
        for a, b, c in faces:
            # OBJ indices are 1-based
            f.write(f"f {a+1} {b+1} {c+1}\n")


def main() -> None:
    vertices, faces = generate_heightmap(25, scale=2.0)
    write_obj(OUTPUT_PATH, vertices, faces)
    print("Saved heightmap mesh to", OUTPUT_PATH)
    print(f"Vertices: {len(vertices)}, Faces: {len(faces)}")


if __name__ == "__main__":
    main()
