# sample2.py
# Simulate a real-time rendering loop and save frame dumps to disk.

import os
import time

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../../temp/realtime_rendering_frames.txt")


def render_frame(width: int, height: int, frame: int) -> str:
    # Simple animation: a dot moving left-to-right and bouncing.
    pos = frame % (width * 2 - 2)
    if pos >= width:
        pos = (width * 2 - 2) - pos
    buffer = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append("O" if x == pos and y == height // 2 else ".")
        buffer.append("".join(row))
    return "\n".join(buffer)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        for frame in range(5):
            f.write(f"Frame {frame}\n")
            f.write(render_frame(40, 10, frame))
            f.write("\n\n")
            time.sleep(0.05)
    print("Saved", OUTPUT_PATH)


if __name__ == "__main__":
    main()
