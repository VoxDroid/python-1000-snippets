# 0296-Virtual-Reality Cheatsheet

## Quick Start
- Generate stereo images:
  - `python python-1000-snippets/0296-Virtual-Reality/SAMPLES/sample1.py`
- Simulate head rotation:
  - `python python-1000-snippets/0296-Virtual-Reality/SAMPLES/sample2.py`
- Create an anaglyph (red/cyan) from stereo images:
  - `python python-1000-snippets/0296-Virtual-Reality/SAMPLES/sample3.py`

## Concepts
- **Stereo Rendering**: Render a scene from two slightly offset eye positions to create depth perception.
- **Head Tracking**: Adjust view projection based on head orientation.
- **Anaglyph**: Combine left/right views into a single image for simple 3D viewing with colored glasses.

## Tips
- Use real-time rendering engines (OpenGL, Vulkan, Unity) for interactive VR.
- Use proper camera intrinsics and calibration for accurate stereo rendering.
- For head tracking, use IMU and pose estimation to update the viewpoints.
