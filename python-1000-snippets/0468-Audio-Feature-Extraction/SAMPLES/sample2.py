# sample2.py
# Compute spectral centroid and bandwidth from a synthetic audio signal.

import numpy as np


def spectral_centroid(signal: np.ndarray, sr: int) -> float:
    magnitude = np.abs(np.fft.rfft(signal))
    freqs = np.fft.rfftfreq(len(signal), 1 / sr)
    return float(np.sum(freqs * magnitude) / np.sum(magnitude))


def spectral_bandwidth(signal: np.ndarray, sr: int) -> float:
    magnitude = np.abs(np.fft.rfft(signal))
    freqs = np.fft.rfftfreq(len(signal), 1 / sr)
    centroid = spectral_centroid(signal, sr)
    return float(np.sqrt(np.sum(((freqs - centroid) ** 2) * magnitude) / np.sum(magnitude)))


def main() -> None:
    sr = 22050
    t = np.linspace(0, 1, sr, endpoint=False)
    # Mix two tones to create a richer spectrum.
    signal = 0.5 * np.sin(2 * np.pi * 440 * t) + 0.3 * np.sin(2 * np.pi * 880 * t)

    print("Spectral centroid (Hz):", round(spectral_centroid(signal, sr), 2))
    print("Spectral bandwidth (Hz):", round(spectral_bandwidth(signal, sr), 2))


if __name__ == "__main__":
    main()
