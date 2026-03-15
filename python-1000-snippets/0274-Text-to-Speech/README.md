# Text to Speech

## Description
This snippet demonstrates generating speech audio from text using TTS libraries.

## Dependencies
- `gtts` (Google Text-to-Speech API)
- `pyttsx3` (offline TTS engine)

Install with:
```bash
pip install gtts pyttsx3
```

## Samples
- `SAMPLES/sample1.py`: Generates an MP3 file using gTTS.
- `SAMPLES/sample2.py`: Uses pyttsx3 to generate a WAV file (offline).
- `SAMPLES/sample3.py`: Generates multiple MP3 files from different phrases using gTTS.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- `gtts` requires network access to call Google’s TTS service.
- `pyttsx3` works offline but depends on system voice engines (e.g., espeak on Linux).
- Output files are saved in the snippet directory.
