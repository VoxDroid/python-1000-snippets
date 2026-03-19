# sample3.py
# Generate a short spectrogram (magnitude) using STFT and summarize energy per frame.

import numpy as np


def stft_magnitude(signal: np.ndarray, frame_size: int = 1024, hop: int = 512):
    frames = []
    for start in range(0, len(signal) - frame_size + 1, hop):
        frame = signal[start : start + frame_size] * np.hanning(frame_size)
        spectrum = np.fft.rfft(frame)
        frames.append(np.abs(spectrum))
    return np.vstack(frames)


def main() -> None:
    sr = 22050
    t = np.linspace(0, 2, sr * 2, endpoint=False)
    signal = 0.4 * np.sin(2 * np.pi * 220 * t) + 0.2 * np.sin(2 * np.pi * 440 * t)

    spec = stft_magnitude(signal)
    energy = np.sum(spec, axis=1)

    print("Spectrogram shape (frames x bins):", spec.shape)
    print("Energy per frame (first 5):", np.round(energy[:5], 2).tolist())


if __name__ == "__main__":
    main()
