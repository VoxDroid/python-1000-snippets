# sample3.py
# Create a multi-tone WAV file and run speech recognition on it.

import wave
import numpy as np
import speech_recognition as sr


def make_tone(freq: float, duration: float, rate: int = 16000):
    t = np.linspace(0, duration, int(rate * duration), False)
    return 0.5 * np.sin(2 * np.pi * freq * t)


def save_wave(filename: str, samples: np.ndarray, rate: int = 16000):
    audio = np.int16(samples * 32767)
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(audio.tobytes())


def recognize_audio(filename: str):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
    try:
        return r.recognize_sphinx(audio_data)
    except sr.UnknownValueError:
        return None


if __name__ == '__main__':
    out_file = 'tone_sequence.wav'

    # Generate a short sequence of tones (like DTMF-like beeps)
    sequence = np.concatenate([
        make_tone(440.0, 0.3),  # A
        np.zeros(1600),         # short pause
        make_tone(554.37, 0.3), # C#
        np.zeros(1600),
        make_tone(659.25, 0.3), # E
    ])

    save_wave(out_file, sequence)

    transcription = recognize_audio(out_file)
    print('Saved', out_file)
    if transcription:
        print('Transcription:', transcription)
    else:
        print('No transcription could be produced for tone sequence.')
