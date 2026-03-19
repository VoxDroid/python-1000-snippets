# 0467-Speech-Synthesis Cheatsheet

## Quick Tips
- Use `pyttsx3` for offline, cross-platform TTS without cloud dependencies.
- Confirm the output path is writable and the engine supports the desired voice.
- Provide a fallback (e.g., generate a simple tone) if the TTS engine is unavailable.

## Running examples
- `python SAMPLES/sample1.py` — synthesize a phrase to a WAV file.
- `python SAMPLES/sample2.py` — list available TTS voices.
- `python SAMPLES/sample3.py` — generate a synthetic sine-wave WAV file as a fallback.
