# Cloth Simulation

## Description
This snippet demonstrates a basic 2D cloth simulation using a mass-spring model with Verlet integration and constraint relaxation.

## Files
- `SAMPLES/sample1.py`: Runs a small cloth simulation and prints key corner coordinates.
- `SAMPLES/sample2.py`: Runs the simulation and saves a visualization image to `/tmp/cloth.png`.
- `SAMPLES/sample3.py`: Adds a wind force and prints kinetic energy to demonstrate external forcing.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Top-left: [0. 0.]
Top-right: [4. 0.]
Bottom-left: [0. 4.]
Bottom-right: [4. 3.7]
Saved /tmp/cloth.png
Kinetic energy: 0.52
```

## Explanation
- **Verlet integration**: computes next positions based on current and previous positions.
- **Constraints**: keeps springs at rest length by correcting point positions.
- **Fixed points**: top row is fixed to simulate hanging cloth.
- **Visualization**: `sample2.py` draws the grid as lines into an image.
