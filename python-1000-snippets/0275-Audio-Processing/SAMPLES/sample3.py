# sample3.py
# Analyze audio spectrum using FFT to find dominant frequency.

import wave
import numpy as np


def load_mono_wav(path):
    with wave.open(path, 'rb') as wf:
        rate = wf.getframerate()
        frames = wf.readframes(wf.getnframes())
        samples = np.frombuffer(frames, dtype=np.int16)
        if wf.getnchannels() > 1:
            samples = samples.reshape(-1, wf.getnchannels())[:, 0]
    return samples, rate


def dominant_frequency(samples, rate):
    n = len(samples)
    fft = np.fft.rfft(samples)
    freqs = np.fft.rfftfreq(n, d=1/rate)
    magnitude = np.abs(fft)
    idx = np.argmax(magnitude)
    return freqs[idx], magnitude[idx]


if __name__ == '__main__':
    path = 'sine_440hz.wav'
    samples, rate = load_mono_wav(path)
    freq, mag = dominant_frequency(samples, rate)
    print(f"Dominant frequency in {path}: {freq:.1f} Hz (magnitude {mag:.0f})")
