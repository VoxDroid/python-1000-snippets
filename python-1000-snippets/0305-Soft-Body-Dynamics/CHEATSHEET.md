# 0305 - Soft Body Dynamics Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use **constraint relaxation** to keep springs close to their rest length.
- Add **damping** to reduce oscillation and stabilize the system.
- For 2D soft bodies, connect each node to its neighbors in a grid and optionally including diagonal springs.
- Measure deformation by comparing current spring lengths to rest lengths.
