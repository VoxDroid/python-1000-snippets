# 0303 - Cloth Simulation Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use **Verlet integration** to stabilize the simulation without explicit velocity tracking.
- Apply **constraint relaxation** by iterating over spring connections and adjusting positions to maintain rest lengths.
- Fix one edge (e.g., top row) to simulate a hanging cloth.
- For visual debugging, render line segments between neighboring cloth particles into an image.
