# sample2.py
# Attempt speech recognition on a provided WAV file (speech_test.wav) or fallback to a generated tone.

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


def transcribe_file(audio_path: str):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
    try:
        return recognizer.recognize_sphinx(audio_data)
    except sr.UnknownValueError:
        return None


if __name__ == '__main__':
    audio_path = 'speech_test.wav'

    try:
        with wave.open(audio_path, 'rb'):
            print('Using existing audio file:', audio_path)
    except FileNotFoundError:
        print('No speech_test.wav found; generating a test tone.')
        generate_tone(audio_path)

    transcription = transcribe_file(audio_path)
    if transcription:
        print('Transcribed text:', transcription)
    else:
        print('No transcription could be produced from audio. (Expected for tones)')
