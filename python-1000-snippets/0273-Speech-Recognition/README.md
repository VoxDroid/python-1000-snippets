# Speech Recognition

## Description
This snippet demonstrates offline speech recognition using `speechrecognition` with the `pocketsphinx` engine.

## Dependencies
- `speechrecognition`
- `pocketsphinx`
- `numpy`

Install with:
```bash
pip install speechrecognition pocketsphinx numpy
```

## Samples
- `SAMPLES/sample1.py`: Generates a short tone WAV file and runs offline transcription.
- `SAMPLES/sample2.py`: Attempts to transcribe `speech_test.wav` if present, otherwise generates a tone file.
- `SAMPLES/sample3.py`: Creates a multi-tone WAV file and runs offline transcription.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- The `pocketsphinx` engine works offline but requires audio that resembles speech. Tone-based audio will usually not transcribe into meaningful text.
- For real speech input, provide a WAV file (`speech_test.wav`) recorded from a microphone or other source.
