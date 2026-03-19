# sample1.py
# Compute basic audio features (RMS and zero-crossing rate) from a synthetic signal.

import numpy as np


def rms(signal: np.ndarray) -> float:
    return float(np.sqrt(np.mean(signal ** 2)))


def zero_crossing_rate(signal: np.ndarray) -> float:
    crossings = np.sum(np.abs(np.diff(np.sign(signal))))
    return float(crossings) / (len(signal) - 1)


def main() -> None:
    sr = 22050
    t = np.linspace(0, 1, sr, endpoint=False)
    signal = 0.5 * np.sin(2 * np.pi * 440 * t)  # A4 tone

    print("RMS:", round(rms(signal), 4))
    print("Zero-crossing rate:", round(zero_crossing_rate(signal), 4))


if __name__ == "__main__":
    main()
