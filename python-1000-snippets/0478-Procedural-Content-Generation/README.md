# Procedural Content Generation

## Description
This snippet demonstrates procedural generation techniques for game worlds using pure Python and NumPy.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Dungeon map (1=wall,0=floor):
............##..........................
............###..........######.....####
..#####.....####........#########..#####
...
```

## Explanation
- **Cellular Automata**: Generates dungeon-like maps by iteratively applying neighborhood rules.
- **Maze Generation**: Uses randomized Prim's algorithm to carve a perfect maze.
- **Heightmap Noise**: Builds a terrain heightmap by layering smoothed random noise.
- **Best Practice**: Seed randomness for repeatability and tune parameters for desired density.
