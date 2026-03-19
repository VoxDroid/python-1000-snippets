# 0464-Pose-Estimation Cheatsheet

## Quick Tips
- Pose estimation can be broken down into keypoint detection and geometric reasoning (angles, distances).
- Normalize keypoints by centering around a reference joint (e.g., hips) and scaling by a body dimension.
- Simple heuristics (e.g., knee height relative to hip) can approximate pose categories.

## Running examples
- `python SAMPLES/sample1.py` — compute a joint angle from synthetic keypoints.
- `python SAMPLES/sample2.py` — classify pose as standing vs crouching.
- `python SAMPLES/sample3.py` — normalize keypoints to a canonical coordinate frame.
