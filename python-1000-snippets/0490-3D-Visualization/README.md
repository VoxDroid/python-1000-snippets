# 3D Visualization

## Description
This snippet demonstrates basic 3D data generation and exporting without requiring a 3D visualization library.
It generates point clouds and mesh files that can be loaded into 3D tools.

## Code
The sample scripts show how to:
- Generate a 3D point cloud and save it as a PLY file (`sample1.py`).
- Generate a heightmap mesh and save it as an OBJ file (`sample2.py`).
- Compute simple mesh statistics (centroid and bounds) (`sample3.py`).

## Output
`sample1.py` writes a PLY point cloud to:
```
python-1000-snippets/temp/cube.ply
```

`sample2.py` writes an OBJ mesh to:
```
python-1000-snippets/temp/heightmap.obj
```

`sample3.py` prints mesh summary statistics, such as centroid and bounds.

## Explanation
- **3D Data Generation**: Constructs basic 3D geometry (cube, heightmap) purely in Python.
- **Logic**: Creates vertex lists, optional face lists, and writes standard 3D file formats (PLY, OBJ).
- **Complexity**: O(n) where n is the number of vertices/faces.
- **Use Case**: Useful for generating test data for 3D tools or learning file formats.