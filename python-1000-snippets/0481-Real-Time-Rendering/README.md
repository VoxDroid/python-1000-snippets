# Real-Time Rendering

## Description
This snippet simulates a real-time rendering loop without requiring a graphics library.
It uses ASCII frames and basic timing to illustrate how a renderer updates frames over time.

## Code
The sample scripts show several approaches:
- `sample1.py`: Renders a single ASCII frame and prints it.
- `sample2.py`: Runs a short loop and writes multiple frame snapshots into `temp/realtime_rendering_frames.txt`.
- `sample3.py`: Measures frame timing and prints an approximate FPS.

## Output
`sample1.py` prints an ASCII frame (e.g., 20x10).

`sample2.py` writes a file such as:
```
temp/realtime_rendering_frames.txt
```

`sample3.py` prints an approximate frame rate, for example:
```
Rendered 120 frames in 0.40s (~300 FPS)
```

## Explanation
- **Real-Time Rendering Loop**: A renderer typically updates frames repeatedly over time.
- **Logic**: Each frame is generated based on a frame counter; output is printed or written to disk.
- **Complexity**: O(width * height * frames) for the full simulation.
- **Use Case**: Useful for understanding frame loops and timing without a real graphics stack.
