# sample3.py
# Render a gradient image using a shader-like function and report pixel statistics.


def generate_gradient(width: int, height: int):
    total = 0.0
    min_val = float("inf")
    max_val = float("-inf")
    for y in range(height):
        for x in range(width):
            nx = x / (width - 1)
            ny = y / (height - 1)
            val = nx * 0.5 + ny * 0.5
            total += val
            min_val = min(min_val, val)
            max_val = max(max_val, val)
    mean_val = total / (width * height)
    return min_val, max_val, mean_val


def main() -> None:
    min_val, max_val, mean_val = generate_gradient(64, 64)
    print("Min value:", min_val)
    print("Max value:", max_val)
    print("Mean value:", mean_val)


if __name__ == "__main__":
    main()
