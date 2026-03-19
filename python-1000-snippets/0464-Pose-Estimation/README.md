# Pose Estimation

## Description
This snippet demonstrates basic pose estimation concepts using synthetic keypoints and geometric operations (no deep learning dependencies).

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Shoulder: [0.2, 0.5]
Elbow: [0.4, 0.4]
Wrist: [0.6, 0.6]
Computed elbow angle (degrees): 108.43
```

## Explanation
- **Pose Estimation**: Predicting body keypoints and computing joint angles or body posture.
- **sample1.py**: Computes the elbow angle from three keypoints.
- **sample2.py**: Classifies a simple pose as standing vs crouching based on hip/knee/ankle positions.
- **sample3.py**: Normalizes keypoints by centering and scaling around the mid-hip.
- **Best Practice**: Use camera calibration to normalize keypoints and validate against annotated datasets.
