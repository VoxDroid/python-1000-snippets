# sample1.py
# Generate a simple sine wave and save it as a WAV file.

import wave
import numpy as np


def generate_sine_wave(freq=440.0, duration=1.0, rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(rate * duration), endpoint=False)
    wave_data = amplitude * np.sin(2 * np.pi * freq * t)
    return (wave_data * 32767).astype(np.int16)


def save_wav(path, samples, rate=44100):
    with wave.open(path, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(samples.tobytes())


if __name__ == '__main__':
    out_path = "sine_440hz.wav"
    samples = generate_sine_wave(freq=440.0, duration=2.0, rate=44100)
    save_wav(out_path, samples)
    rms = np.sqrt(np.mean(samples.astype(np.float64) ** 2))
    print(f"Saved {out_path} (RMS={rms:.2f})")
