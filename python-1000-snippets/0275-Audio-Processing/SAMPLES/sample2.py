# sample2.py
# Load a WAV file and compute basic audio statistics.

import wave
import numpy as np


def load_wav(path):
    with wave.open(path, 'rb') as wf:
        n_channels = wf.getnchannels()
        rate = wf.getframerate()
        n_frames = wf.getnframes()
        raw = wf.readframes(n_frames)

    audio = np.frombuffer(raw, dtype=np.int16)
    if n_channels > 1:
        audio = audio.reshape(-1, n_channels)
    return audio, rate


if __name__ == '__main__':
    in_path = 'sine_440hz.wav'
    try:
        audio, rate = load_wav(in_path)
    except FileNotFoundError:
        print(f"File not found: {in_path}")
        raise

    duration = len(audio) / rate
    rms = np.sqrt(np.mean(audio.astype(np.float64) ** 2))
    peak = np.max(np.abs(audio))

    print(f"Loaded {in_path}")
    print(f"Sample rate: {rate} Hz")
    print(f"Duration: {duration:.3f} seconds")
    print(f"RMS: {rms:.2f}")
    print(f"Peak: {peak}")
