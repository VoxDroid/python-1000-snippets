# sample1.py
# Simple "real-time" rendering simulation using ASCII frames.

import time


def render_frame(width: int, height: int, frame: int) -> str:
    # Create a simple moving dot pattern.
    buffer = []
    for y in range(height):
        row = []
        for x in range(width):
            if (x + y + frame) % 10 == 0:
                row.append("O")
            else:
                row.append(".")
        buffer.append("".join(row))
    return "\n".join(buffer)


def main() -> None:
    frame = 0
    # Print a single frame to keep output deterministic.
    print(render_frame(20, 10, frame))
    print("(Rendered frame #", frame, ")")


if __name__ == "__main__":
    main()
