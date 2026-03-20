# 3D Point Cloud Processing

## Description
This snippet demonstrates basic 3D point cloud processing tasks using NumPy: voxel downsampling, normal estimation, and bounding-box operations.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Original point count: 500
Downsampled point count: 483
Sample downsampled points (first 3):
  [5.488, 7.152, 6.028]
  [5.449, 4.237, 6.459]
  [4.376, 8.918, 9.637]
```

## Explanation
- **Point Cloud Processing**: Manipulates 3D point clouds for 3D scanning and robotics.
- **sample1.py**: Applies a voxel grid downsampling.
- **sample2.py**: Estimates normals using PCA on local neighbors.
- **sample3.py**: Computes axis-aligned bounding boxes and applies a translation.
- **Best Practice**: Use spatial indexing (KD-tree) for large point clouds, and validate normals orientation.
