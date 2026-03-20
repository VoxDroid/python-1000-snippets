# sample3.py
# Simulate a frame loop and report average frame time (fps) for a simple renderer.

import time


def render_step(width: int, height: int, frame: int) -> None:
    # Perform lightweight work to simulate rendering.
    # We update a small buffer but do not output it.
    for y in range(height):
        for x in range(width):
            _ = (x + y + frame) % 256


def main() -> None:
    frames = 120
    width, height = 80, 40
    start = time.perf_counter()
    for frame in range(frames):
        render_step(width, height, frame)
    elapsed = time.perf_counter() - start
    fps = frames / elapsed if elapsed > 0 else float('inf')
    print(f"Rendered {frames} frames in {elapsed:.3f}s (~{fps:.1f} FPS)")


if __name__ == "__main__":
    main()
