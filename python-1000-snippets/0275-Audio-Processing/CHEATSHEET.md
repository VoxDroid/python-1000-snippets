# 0275 - Audio Processing Cheatsheet

## Quick Commands
```bash
pip install numpy
python SAMPLES/sample1.py  # Generate a sine wave WAV
python SAMPLES/sample2.py  # Load WAV and compute stats
python SAMPLES/sample3.py  # Find dominant frequency using FFT
```

## Tips
- Use `wave` to read/write WAV files and `numpy` to manipulate samples.
- RMS amplitude: `np.sqrt(np.mean(samples**2))`.
- Dominant frequency: use `np.fft.rfft` and `np.fft.rfftfreq`.
