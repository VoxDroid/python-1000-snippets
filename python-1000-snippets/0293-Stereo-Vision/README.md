# Stereo Vision

## Description
This snippet demonstrates basic stereo vision techniques using OpenCV.

## Samples
- `SAMPLES/sample1.py`: Compute a disparity map from a synthetic stereo pair using StereoBM.
- `SAMPLES/sample2.py`: Convert disparity to depth using a simple pinhole camera model.
- `SAMPLES/sample3.py`: Compare StereoBM and StereoSGBM disparity estimators.

## Running
```bash
python python-1000-snippets/0293-Stereo-Vision/SAMPLES/sample1.py
python python-1000-snippets/0293-Stereo-Vision/SAMPLES/sample2.py
python python-1000-snippets/0293-Stereo-Vision/SAMPLES/sample3.py
```

## Notes
- These examples use synthetic images for deterministic results.
- In real applications, supply rectified stereo images and calibrate cameras.
