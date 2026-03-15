# Audio Processing

## Description
This snippet demonstrates basic audio processing using standard Python libraries (`wave`, `numpy`). It generates a waveform, reads a WAV file, and performs basic spectral analysis.

## Dependencies
- `numpy`

Install with:
```bash
pip install numpy
```

## Samples
- `SAMPLES/sample1.py`: Generate a sine wave and save it as a WAV file.
- `SAMPLES/sample2.py`: Load a WAV file and compute duration, RMS, and peak amplitude.
- `SAMPLES/sample3.py`: Analyze the dominant frequency of a WAV file using FFT.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- The generated WAV file (`sine_440hz.wav`) is used as input for analysis in the other samples.
- You can replace `sine_440hz.wav` with any mono WAV file for analysis.
