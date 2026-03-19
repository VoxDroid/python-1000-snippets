# Speech Synthesis

## Description
This snippet demonstrates simple offline speech synthesis using `pyttsx3`, with a fallback to generate a synthetic sine wave audio file.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Saved speech to /.../temp/tts_sample.wav
```

## Explanation
- **Speech Synthesis**: Converts text into audio.
- **sample1.py**: Uses `pyttsx3` to save a spoken sentence as a WAV file.
- **sample2.py**: Lists available voices from the TTS engine.
- **sample3.py**: Generates a fallback sine wave WAV file if TTS is unavailable.
- **Best Practice**: Use offline TTS engines for reproducibility in offline/CI environments, and validate audio output path and format.
