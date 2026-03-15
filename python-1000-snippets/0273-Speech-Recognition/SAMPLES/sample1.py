# sample1.py
# Run offline speech recognition using pocketsphinx on a generated audio file.

import wave
import numpy as np
import speech_recognition as sr


def generate_tone(filename: str, duration: float = 1.0, freq: float = 440.0, rate: int = 16000):
    t = np.linspace(0, duration, int(rate * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * freq * t)
    audio = np.int16(tone * 32767)

    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(audio.tobytes())


if __name__ == '__main__':
    audio_path = 'speech_sample.wav'
    generate_tone(audio_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_sphinx(audio_data)
        print('Recognized text:', text)
    except sr.UnknownValueError:
        print('Speech not understood (as expected for a tone).')
    except Exception as e:
        print('Error during recognition:', e)
