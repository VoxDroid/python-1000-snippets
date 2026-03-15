# 0274 - Text to Speech Cheatsheet

## Quick Commands
```bash
pip install gtts pyttsx3
python SAMPLES/sample1.py  # gTTS -> MP3
python SAMPLES/sample2.py  # pyttsx3 -> WAV
python SAMPLES/sample3.py  # multiple gTTS files
```

## Tips
- `gtts` uses Google’s online TTS service; it requires network connectivity.
- `pyttsx3` works offline but depends on a system TTS backend (espeak/mbrola/etc.).
- Output files are written to the snippet directory (e.g., `hello_tts.mp3`).
