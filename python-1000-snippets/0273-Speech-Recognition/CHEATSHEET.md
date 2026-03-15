# 0273-Speech Recognition Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py  # Generate tone + run pocketsphinx
python SAMPLES/sample2.py  # Transcribe speech_test.wav if present, else generate tone
python SAMPLES/sample3.py  # Generate multi-tone WAV and run pocketsphinx
```

## Notes
- Uses **offline** recognition via `pocketsphinx` (no network needed).
- Best results come from real spoken audio (WAV, 16kHz mono).
- For most synthetic tones, transcription will fail and return nothing.

## Tips
- Provide a WAV file named `speech_test.wav` in the snippet directory to test with your own audio.
- Use `speech_recognition.Recognizer().record()` to load audio and `RecognizeSphinx` for offline transcription.
