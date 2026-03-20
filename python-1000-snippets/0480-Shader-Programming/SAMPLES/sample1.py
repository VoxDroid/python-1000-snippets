# sample1.py
# Generate a simple shader-like image and save it as a PPM file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../../temp/shader_output.ppm")


def generate_shader_image(width: int = 256, height: int = 256):
    # Procedural color based on normalized coordinates
    img = []
    for y in range(height):
        for x in range(width):
            nx = x / (width - 1)
            ny = y / (height - 1)
            r = int(255 * nx)
            g = int(255 * ny)
            b = int(255 * (0.5 + 0.5 * (nx - ny)))
            img.append((r, g, b))
    return img


def save_ppm(path: str, width: int, height: int, pixels):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(f"P3\n{width} {height}\n255\n")
        for r, g, b in pixels:
            f.write(f"{r} {g} {b} ")


def main() -> None:
    width, height = 128, 128
    pixels = generate_shader_image(width, height)
    save_ppm(OUTPUT_PATH, width, height, pixels)
    print("Saved shader output to", OUTPUT_PATH)


if __name__ == "__main__":
    main()
