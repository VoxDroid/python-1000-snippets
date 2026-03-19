# sample3.py
# Fallback audio generation: write a simple sine wave to a WAV file.

import os
import wave
import struct
import math

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../../temp/tts_sine.wav")


def generate_sine_wav(path: str, duration_s: float = 1.0, freq_hz: float = 440.0, rate: int = 22050):
    n_samples = int(duration_s * rate)
    amplitude = 0.3 * (2**15 - 1)

    with wave.open(path, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        for i in range(n_samples):
            sample = amplitude * math.sin(2 * math.pi * freq_hz * (i / rate))
            wf.writeframes(struct.pack("h", int(sample)))


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    generate_sine_wav(OUTPUT_PATH)
    print(f"Generated sine wave audio at {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
