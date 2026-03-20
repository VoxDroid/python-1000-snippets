# 0476-3D-Point-Cloud-Processing Cheatsheet

## Quick Tips
- Use voxel grid downsampling to reduce point cloud density while preserving structure.
- Estimate normals via PCA on local neighborhoods; a KD-tree can speed up neighbor queries.
- Compute axis-aligned bounding boxes to quickly understand the spatial extent.

## Running examples
- `python SAMPLES/sample1.py` — voxel downsampling of a random point cloud.
- `python SAMPLES/sample2.py` — normal estimation using local PCA.
- `python SAMPLES/sample3.py` — bounding box computation and point translation.
