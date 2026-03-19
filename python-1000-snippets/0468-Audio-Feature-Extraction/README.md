# Audio Feature Extraction

## Description
This snippet demonstrates extracting basic audio features (RMS, zero crossing, spectral centroid, and spectrogram energy) using NumPy and SciPy.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
RMS: 0.3536
Zero-crossing rate: 0.0798
```

## Explanation
- **Audio Feature Extraction**: Derives numerical features from audio for analysis or ML.
- **sample1.py**: Computes RMS (energy) and zero-crossing rate from a synthetic tone.
- **sample2.py**: Computes spectral centroid and bandwidth via FFT.
- **sample3.py**: Computes a simple spectrogram and summarizes per-frame energy.
- **Best Practice**: Normalize audio, use windowing, and validate features on real recordings.
